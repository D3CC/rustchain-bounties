# Policy Declaration: One Canonical RTC Wallet Per Contributor Identity

**Effective Date:** 2026-04-27  
**Compliance Deadline:** 2026-05-11  
**Scope:** All contributors to RustChain Bounties (github.com/Scottcjn/rustchain-bounties)

## TL;DR

If you have **two GitHub accounts citing the same RTC wallet** — or **two RTC wallets cited from the same GitHub account** — you must **declare ONE canonical payout wallet within 14 days (by 2026-05-11)**. Otherwise, the RustChain Bounties system will infer per-PR (per-pull-request) wallet assignments.

## Background

A forensic audit conducted on 2026-04-27 identified **5 contributors** with conflicting wallet registrations:

1. **Multi-account single-wallet:** A contributor using two GitHub accounts both pointing to the same RTC wallet address.
2. **Single-account multi-wallet:** A contributor using one GitHub account but listing two different RTC wallet addresses across different bounties or PRs.

These conflicts create ambiguity in payout routing and increase administrative overhead for bounty settlement.

## Policy Details

### 1. Requirement

Every contributor identity (defined as a unique combination of GitHub account + verified email) must be associated with **exactly one canonical RTC wallet address**.

### 2. Declaration Process

To declare your canonical wallet:

- **Step 1:** Navigate to your GitHub profile settings.
- **Step 2:** Update your profile bio or a pinned repository's `README.md` to include:
  ```
  RTC Wallet: <your_single_wallet_address>
  ```
- **Step 3:** If you have multiple GitHub accounts, choose one primary account and update its bio. Remove wallet references from secondary accounts.
- **Step 4:** If you have multiple wallets, choose one and update all PR descriptions and bounty claim comments to reference only that wallet.

### 3. Deadline

All declarations must be completed by **2026-05-11 23:59 UTC**.

### 4. Consequences of Non-Compliance

If no declaration is made by the deadline:

- The system will apply **per-PR inference**: each PR will be paid to the wallet address most recently associated with that specific PR.
- This may result in **split payments** across multiple wallets for the same contributor.
- No retroactive consolidation will be performed.

### 5. Verification

After the deadline, a second audit will be conducted on 2026-05-12. Contributors who have complied will have their canonical wallet recorded in the `CONTRIBUTORS.yaml` file in this repository.

## Example: Correct Declaration

**Before (conflicting):**
```yaml
# In PR #42 description
RTC Wallet: 0x1234...abcd

# In PR #58 description
RTC Wallet: 0x5678...efgh
```

**After (canonical):**
```yaml
# In PR #42 description
RTC Wallet: 0x1234...abcd

# In PR #58 description
RTC Wallet: 0x1234...abcd

# In GitHub profile bio
RTC Wallet: 0x1234...abcd
```

## Technical Implementation

The canonical wallet resolution will be enforced via a GitHub Actions workflow that runs after the deadline. Below is the verification script that will be executed:

```yaml
# .github/workflows/verify-canonical-wallet.yml
name: Verify Canonical Wallet

on:
  schedule:
    - cron: '0 0 12 5 *'  # Runs on May 12 annually
  workflow_dispatch:

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check wallet consistency
        run: |
          python3 -c "
          import yaml
          import sys

          with open('CONTRIBUTORS.yaml', 'r') as f:
              data = yaml.safe_load(f)

          errors = []
          for contributor in data['contributors']:
              wallets = set()
              for entry in contributor.get('prs', []):
                  wallets.add(entry.get('wallet'))
              if len(wallets) > 1:
                  errors.append(f'{contributor[\"github\"]}: {len(wallets)} wallets found')

          if errors:
              print('Non-compliant contributors:')
              for e in errors:
                  print(f'  - {e}')
              sys.exit(1)
          else:
              print('All contributors compliant.')
          "
```

## FAQ

**Q: What if I have a legitimate reason for multiple wallets?**  
A: Contact the maintainers via a GitHub issue with label `wallet-exception` before the deadline. Exceptions are granted only for documented technical reasons (e.g., wallet migration in progress).

**Q: Can I change my canonical wallet after declaring it?**  
A: Yes, but you must update all references and notify the maintainers. A new declaration period may be opened if needed.

**Q: What happens to pending payouts during the declaration period?**  
A: All payouts are frozen until the deadline. After declaration, payouts will resume using the canonical wallet.

## References

- [RustChain Bounties README](https://github.com/Scottcjn/rustchain-bounties)
- [Contributing Guide](https://github.com/Scottcjn/rustchain-bounties/blob/main/CONTRIBUTING.md)
- [Bounty Issue Tracker](https://github.com/Scottcjn/rustchain-bounties/issues?q=is%3Aissue+is%3Aopen+label%3Abounty)

---

*This policy is enforced by the RustChain Bounties maintainers. For questions, open an issue with the `policy` label.*