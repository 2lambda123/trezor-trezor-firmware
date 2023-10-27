# generated from __init__.py.mako
# do not edit manually!
from typing import TYPE_CHECKING

from trezor.wire import DataError

from ..types import AccountTemplate, InstructionIdFormat, PropertyTemplate, UIProperty
from .instruction import Instruction

if TYPE_CHECKING:
    from typing import Any, Type

    from ..types import Account

SYSTEM_PROGRAM_ID = "11111111111111111111111111111111"
STAKE_PROGRAM_ID = "Stake11111111111111111111111111111111111111"
COMPUTE_BUDGET_PROGRAM_ID = "ComputeBudget111111111111111111111111111111"
TOKEN_PROGRAM_ID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
TOKEN_2022_PROGRAM_ID = "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"
ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID = "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
MEMO_PROGRAM_ID = "MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr"
MEMO_LEGACY_PROGRAM_ID = "Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo"

SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT = 0
SYSTEM_PROGRAM_ID_INS_ASSIGN = 1
SYSTEM_PROGRAM_ID_INS_TRANSFER = 2
SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT_WITH_SEED = 3
SYSTEM_PROGRAM_ID_INS_ADVANCE_NONCE_ACCOUNT = 4
SYSTEM_PROGRAM_ID_INS_WITHDRAW_NONCE_ACCOUNT = 5
SYSTEM_PROGRAM_ID_INS_INITIALIZE_NONCE_ACCOUNT = 6
SYSTEM_PROGRAM_ID_INS_AUTHORIZE_NONCE_ACCOUNT = 7
SYSTEM_PROGRAM_ID_INS_ALLOCATE = 8
SYSTEM_PROGRAM_ID_INS_ALLOCATE_WITH_SEED = 9
SYSTEM_PROGRAM_ID_INS_ASSIGN_WITH_SEED = 10
SYSTEM_PROGRAM_ID_INS_TRANSFER_WITH_SEED = 11
SYSTEM_PROGRAM_ID_INS_UPGRADE_NONCE_ACCOUNT = 12
STAKE_PROGRAM_ID_INS_INITIALIZE = 0
STAKE_PROGRAM_ID_INS_AUTHORIZE = 1
STAKE_PROGRAM_ID_INS_DELEGATE_STAKE = 2
STAKE_PROGRAM_ID_INS_SPLIT = 3
STAKE_PROGRAM_ID_INS_WITHDRAW = 4
STAKE_PROGRAM_ID_INS_DEACTIVATE = 5
STAKE_PROGRAM_ID_INS_SET_LOCKUP = 6
STAKE_PROGRAM_ID_INS_MERGE = 7
STAKE_PROGRAM_ID_INS_AUTHORIZE_WITH_SEED = 8
STAKE_PROGRAM_ID_INS_INITIALIZE_CHECKED = 9
STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED = 10
STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED_WITH_SEED = 11
STAKE_PROGRAM_ID_INS_SET_LOCKUP_CHECKED = 12
COMPUTE_BUDGET_PROGRAM_ID_INS_REQUEST_HEAP_FRAME = 1
COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT = 2
COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE = 3
TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT = 1
TOKEN_PROGRAM_ID_INS_INITIALIZE_MULTISIG = 2
TOKEN_PROGRAM_ID_INS_TRANSFER = 3
TOKEN_PROGRAM_ID_INS_APPROVE = 4
TOKEN_PROGRAM_ID_INS_REVOKE = 5
TOKEN_PROGRAM_ID_INS_SET_AUTHORITY = 6
TOKEN_PROGRAM_ID_INS_MINT_TO = 7
TOKEN_PROGRAM_ID_INS_BURN = 8
TOKEN_PROGRAM_ID_INS_CLOSE_ACCOUNT = 9
TOKEN_PROGRAM_ID_INS_FREEZE_ACCOUNT = 10
TOKEN_PROGRAM_ID_INS_THAW_ACCOUNT = 11
TOKEN_PROGRAM_ID_INS_TRANSFER_CHECKED = 12
TOKEN_PROGRAM_ID_INS_APPROVE_CHECKED = 13
TOKEN_PROGRAM_ID_INS_MINT_TO_CHECKED = 14
TOKEN_PROGRAM_ID_INS_BURN_CHECKED = 15
TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2 = 16
TOKEN_PROGRAM_ID_INS_SYNC_NATIVE = 17
TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3 = 18
TOKEN_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER = 22
TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT = 1
TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_MULTISIG = 2
TOKEN_2022_PROGRAM_ID_INS_TRANSFER = 3
TOKEN_2022_PROGRAM_ID_INS_APPROVE = 4
TOKEN_2022_PROGRAM_ID_INS_REVOKE = 5
TOKEN_2022_PROGRAM_ID_INS_SET_AUTHORITY = 6
TOKEN_2022_PROGRAM_ID_INS_MINT_TO = 7
TOKEN_2022_PROGRAM_ID_INS_BURN = 8
TOKEN_2022_PROGRAM_ID_INS_CLOSE_ACCOUNT = 9
TOKEN_2022_PROGRAM_ID_INS_FREEZE_ACCOUNT = 10
TOKEN_2022_PROGRAM_ID_INS_THAW_ACCOUNT = 11
TOKEN_2022_PROGRAM_ID_INS_TRANSFER_CHECKED = 12
TOKEN_2022_PROGRAM_ID_INS_APPROVE_CHECKED = 13
TOKEN_2022_PROGRAM_ID_INS_MINT_TO_CHECKED = 14
TOKEN_2022_PROGRAM_ID_INS_BURN_CHECKED = 15
TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2 = 16
TOKEN_2022_PROGRAM_ID_INS_SYNC_NATIVE = 17
TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3 = 18
TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER = 22
ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE = 0
ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE_IDEMPOTENT = 1
ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_RECOVER_NESTED = 2
MEMO_PROGRAM_ID_INS_MEMO = 0
MEMO_LEGACY_PROGRAM_ID_INS_MEMO = 0


def __getattr__(name: str) -> Type[Instruction]:
    def get_id(name: str) -> (str, int):
        if name == "SystemProgramCreateAccountInstruction":
            return ("11111111111111111111111111111111", 0)
        if name == "SystemProgramAssignInstruction":
            return ("11111111111111111111111111111111", 1)
        if name == "SystemProgramTransferInstruction":
            return ("11111111111111111111111111111111", 2)
        if name == "SystemProgramCreateAccountWithSeedInstruction":
            return ("11111111111111111111111111111111", 3)
        if name == "SystemProgramAdvancenonceaccountInstruction":
            return ("11111111111111111111111111111111", 4)
        if name == "SystemProgramWithdrawnonceaccountInstruction":
            return ("11111111111111111111111111111111", 5)
        if name == "SystemProgramInitializenonceaccountInstruction":
            return ("11111111111111111111111111111111", 6)
        if name == "SystemProgramAuthorizenonceaccountInstruction":
            return ("11111111111111111111111111111111", 7)
        if name == "SystemProgramAllocateInstruction":
            return ("11111111111111111111111111111111", 8)
        if name == "SystemProgramAllocateWithSeedInstruction":
            return ("11111111111111111111111111111111", 9)
        if name == "SystemProgramAssignWithSeedInstruction":
            return ("11111111111111111111111111111111", 10)
        if name == "SystemProgramTransferWithSeedInstruction":
            return ("11111111111111111111111111111111", 11)
        if name == "SystemProgramUpgradeNonceAccountInstruction":
            return ("11111111111111111111111111111111", 12)
        if name == "StakeProgramInitializeInstruction":
            return ("Stake11111111111111111111111111111111111111", 0)
        if name == "StakeProgramAuthorizeInstruction":
            return ("Stake11111111111111111111111111111111111111", 1)
        if name == "StakeProgramDelegateStakeInstruction":
            return ("Stake11111111111111111111111111111111111111", 2)
        if name == "StakeProgramSplitInstruction":
            return ("Stake11111111111111111111111111111111111111", 3)
        if name == "StakeProgramWithdrawInstruction":
            return ("Stake11111111111111111111111111111111111111", 4)
        if name == "StakeProgramDeactivateInstruction":
            return ("Stake11111111111111111111111111111111111111", 5)
        if name == "StakeProgramSetLockupInstruction":
            return ("Stake11111111111111111111111111111111111111", 6)
        if name == "StakeProgramMergeInstruction":
            return ("Stake11111111111111111111111111111111111111", 7)
        if name == "StakeProgramAuthorizeWithSeedInstruction":
            return ("Stake11111111111111111111111111111111111111", 8)
        if name == "StakeProgramInitializeCheckedInstruction":
            return ("Stake11111111111111111111111111111111111111", 9)
        if name == "StakeProgramAuthorizeCheckedInstruction":
            return ("Stake11111111111111111111111111111111111111", 10)
        if name == "StakeProgramAuthorizeCheckedWithSeedInstruction":
            return ("Stake11111111111111111111111111111111111111", 11)
        if name == "StakeProgramSetLockupCheckedInstruction":
            return ("Stake11111111111111111111111111111111111111", 12)
        if name == "ComputeBudgetProgramRequestHeapFrameInstruction":
            return ("ComputeBudget111111111111111111111111111111", 1)
        if name == "ComputeBudgetProgramSetComputeUnitLimitInstruction":
            return ("ComputeBudget111111111111111111111111111111", 2)
        if name == "ComputeBudgetProgramSetComputeUnitPriceInstruction":
            return ("ComputeBudget111111111111111111111111111111", 3)
        if name == "TokenProgramInitializeAccountInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 1)
        if name == "TokenProgramInitializeMultisigInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 2)
        if name == "TokenProgramTransferInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 3)
        if name == "TokenProgramApproveInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 4)
        if name == "TokenProgramRevokeInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 5)
        if name == "TokenProgramSetAuthorityInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 6)
        if name == "TokenProgramMinttoInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 7)
        if name == "TokenProgramBurnInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 8)
        if name == "TokenProgramCloseAccountInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 9)
        if name == "TokenProgramFreezeAccountInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 10)
        if name == "TokenProgramThawAccountInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 11)
        if name == "TokenProgramTransferCheckedInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 12)
        if name == "TokenProgramApproveCheckedInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 13)
        if name == "TokenProgramMinttoCheckedInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 14)
        if name == "TokenProgramBurnCheckedInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 15)
        if name == "TokenProgramInitializeAccount2Instruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 16)
        if name == "TokenProgramSyncNativeInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 17)
        if name == "TokenProgramInitializeAccount3Instruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 18)
        if name == "TokenProgramInitializeImmutableOwnerInstruction":
            return ("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 22)
        if name == "Token2022ProgramInitializeAccountInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 1)
        if name == "Token2022ProgramInitializeMultisigInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 2)
        if name == "Token2022ProgramTransferInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 3)
        if name == "Token2022ProgramApproveInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 4)
        if name == "Token2022ProgramRevokeInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 5)
        if name == "Token2022ProgramSetAuthorityInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 6)
        if name == "Token2022ProgramMinttoInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 7)
        if name == "Token2022ProgramBurnInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 8)
        if name == "Token2022ProgramCloseAccountInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 9)
        if name == "Token2022ProgramFreezeAccountInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 10)
        if name == "Token2022ProgramThawAccountInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 11)
        if name == "Token2022ProgramTransferCheckedInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 12)
        if name == "Token2022ProgramApproveCheckedInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 13)
        if name == "Token2022ProgramMinttoCheckedInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 14)
        if name == "Token2022ProgramBurnCheckedInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 15)
        if name == "Token2022ProgramInitializeAccount2Instruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 16)
        if name == "Token2022ProgramSyncNativeInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 17)
        if name == "Token2022ProgramInitializeAccount3Instruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 18)
        if name == "Token2022ProgramInitializeImmutableOwnerInstruction":
            return ("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb", 22)
        if name == "AssociatedTokenAccountProgramCreateInstruction":
            return ("ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL", 0)
        if name == "AssociatedTokenAccountProgramCreateIdempotentInstruction":
            return ("ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL", 1)
        if name == "AssociatedTokenAccountProgramRecoverNestedInstruction":
            return ("ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL", 2)
        if name == "MemoProgramMemoInstruction":
            return ("MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr", 0)
        if name == "MemoLegacyProgramMemoInstruction":
            return ("Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo", 0)
        raise AttributeError(f"Unknown instruction: {name}")

    id = get_id(name)

    class FakeClass(Instruction):
        @classmethod
        def is_type_of(cls, ins: Any):
            return ins.program_id == id[0] and ins.instruction_id == id[1]

    return FakeClass


if TYPE_CHECKING:

    class SystemProgramCreateAccountInstruction(Instruction):
        lamports: int
        space: int
        owner: Account

        funding_account: Account
        new_account: Account

    class SystemProgramAssignInstruction(Instruction):
        owner: Account

        assigned_account: Account

    class SystemProgramTransferInstruction(Instruction):
        lamports: int

        funding_account: Account
        recipient_account: Account

    class SystemProgramCreateAccountWithSeedInstruction(Instruction):
        base: int
        seed: str
        lamports: int
        space: int
        owner: int

        funding_account: Account
        created_account: Account
        base_account: Account | None

    class SystemProgramAdvancenonceaccountInstruction(Instruction):

        nonce_account: Account
        recent_blockhashes_sysvar: Account
        nonce_authority: Account

    class SystemProgramWithdrawnonceaccountInstruction(Instruction):
        lamports: int

        nonce_account: Account
        recipient_account: Account
        recent_blockhashes_sysvar: Account
        rent_sysvar: Account
        nonce_authority: Account

    class SystemProgramInitializenonceaccountInstruction(Instruction):
        nonce_authority: Account

        nonce_account: Account
        recent_blockhashes_sysvar: Account
        rent_sysvar: Account

    class SystemProgramAuthorizenonceaccountInstruction(Instruction):
        nonce_authority: Account

        nonce_account: Account
        nonce_authority: Account

    class SystemProgramAllocateInstruction(Instruction):
        space: int

        new_account: Account

    class SystemProgramAllocateWithSeedInstruction(Instruction):
        base: int
        seed: str
        space: int
        owner: int

        allocated_account: Account
        base_account: Account

    class SystemProgramAssignWithSeedInstruction(Instruction):
        base: int
        seed: str
        owner: int

        assigned_account: Account
        base_account: Account

    class SystemProgramTransferWithSeedInstruction(Instruction):
        lamports: int
        from_seed: str
        from_owner: int

        funding_account: Account
        base_account: Account
        recipient_account: Account

    class SystemProgramUpgradeNonceAccountInstruction(Instruction):

        nonce_account: Account

    class StakeProgramInitializeInstruction(Instruction):
        staker: Account
        withdrawer: Account
        unix_timestamp: int
        epoch: int
        custodian: Account

        uninitialized_stake_account: Account
        rent_sysvar: Account

    class StakeProgramAuthorizeInstruction(Instruction):
        pubkey: int
        stake_authorize: int

        stake_account: Account
        clock_sysvar: Account
        stake_or_withdraw_authority: Account
        lockup_authority: Account | None

    class StakeProgramDelegateStakeInstruction(Instruction):

        initialized_stake_account: Account
        vote_account: Account
        clock_sysvar: Account
        stake_history_sysvar: Account
        config_account: Account
        stake_authority: Account

    class StakeProgramSplitInstruction(Instruction):
        lamports: int

        stake_account: Account
        uninitialized_stake_account: Account
        stake_authority: Account

    class StakeProgramWithdrawInstruction(Instruction):
        lamports: int

        stake_account: Account
        recipient_account: Account
        clock_sysvar: Account
        stake_history_sysvar: Account
        withdrawal_authority: Account
        lockup_authority: Account | None

    class StakeProgramDeactivateInstruction(Instruction):

        delegated_stake_account: Account
        clock_sysvar: Account
        stake_authority: Account

    class StakeProgramSetLockupInstruction(Instruction):
        unix_timestamp: int
        epoch: int
        custodian: int

        initialized_stake_account: Account
        lockup_or_withdraw_authority: Account

    class StakeProgramMergeInstruction(Instruction):

        destination_stake_account: Account
        source_stake_account: Account
        clock_sysvar: Account
        stake_history_sysvar: Account
        stake_authority: Account

    class StakeProgramAuthorizeWithSeedInstruction(Instruction):
        new_authorized_pubkey: int
        stake_authorize: int
        authority_seed: str
        authority_owner: int

        stake_account: Account
        stake_or_withdraw_authority: Account
        clock_sysvar: Account
        lockup_authority: Account | None

    class StakeProgramInitializeCheckedInstruction(Instruction):

        uninitialized_stake_account: Account
        rent_sysvar: Account
        stake_authority: Account
        withdrawal_authority: Account

    class StakeProgramAuthorizeCheckedInstruction(Instruction):
        stake_authorize: int

        stake_account: Account
        clock_sysvar: Account
        stake_or_withdraw_authority: Account
        new_stake_or_withdraw_authority: Account
        lockup_authority: Account | None

    class StakeProgramAuthorizeCheckedWithSeedInstruction(Instruction):
        stake_authorize: int
        authority_seed: str
        authority_owner: int

        stake_account: Account
        stake_or_withdraw_authority: Account
        clock_sysvar: Account
        new_stake_or_withdraw_authority: Account
        lockup_authority: Account | None

    class StakeProgramSetLockupCheckedInstruction(Instruction):
        unix_timestamp: int
        epoch: int

        stake_account: Account
        lockup_or_withdraw_authority: Account
        new_lockup_authority: Account | None

    class ComputeBudgetProgramRequestHeapFrameInstruction(Instruction):
        bytes: int

    class ComputeBudgetProgramSetComputeUnitLimitInstruction(Instruction):
        units: int

    class ComputeBudgetProgramSetComputeUnitPriceInstruction(Instruction):
        lamports: int

    class TokenProgramInitializeAccountInstruction(Instruction):

        account_to_initialize: Account
        mint_account: Account
        owner: Account
        rent_sysvar: Account

    class TokenProgramInitializeMultisigInstruction(Instruction):
        number_of_signers: int

        multisig_account: Account
        rent_sysvar: Account
        signer_accounts: Account

    class TokenProgramTransferInstruction(Instruction):
        amount: int

        source_account: Account
        destination_account: Account
        owner: Account

    class TokenProgramApproveInstruction(Instruction):
        amount: int

        source_account: Account
        delegate_account: Account
        owner: Account

    class TokenProgramRevokeInstruction(Instruction):

        source_account: Account
        owner: Account

    class TokenProgramSetAuthorityInstruction(Instruction):
        authority_type: int
        new_authority: Account

        mint_account: Account
        current_authority: Account

    class TokenProgramMinttoInstruction(Instruction):
        amount: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class TokenProgramBurnInstruction(Instruction):
        amount: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class TokenProgramCloseAccountInstruction(Instruction):

        account_to_close: Account
        destination_account: Account
        owner: Account

    class TokenProgramFreezeAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class TokenProgramThawAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class TokenProgramTransferCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        destination_account: Account
        owner: Account

    class TokenProgramApproveCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        delegate: Account
        owner: Account

    class TokenProgramMinttoCheckedInstruction(Instruction):
        amount: int
        decimals: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class TokenProgramBurnCheckedInstruction(Instruction):
        amount: int
        decimals: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class TokenProgramInitializeAccount2Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account
        rent_sysvar: Account

    class TokenProgramSyncNativeInstruction(Instruction):

        token_account: Account

    class TokenProgramInitializeAccount3Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account

    class TokenProgramInitializeImmutableOwnerInstruction(Instruction):

        account_to_initialize: Account

    class Token2022ProgramInitializeAccountInstruction(Instruction):

        account_to_initialize: Account
        mint_account: Account
        owner: Account
        rent_sysvar: Account

    class Token2022ProgramInitializeMultisigInstruction(Instruction):
        number_of_signers: int

        multisig_account: Account
        rent_sysvar: Account
        signer_accounts: Account

    class Token2022ProgramTransferInstruction(Instruction):
        amount: int

        source_account: Account
        destination_account: Account
        owner: Account

    class Token2022ProgramApproveInstruction(Instruction):
        amount: int

        source_account: Account
        delegate_account: Account
        owner: Account

    class Token2022ProgramRevokeInstruction(Instruction):

        source_account: Account
        owner: Account

    class Token2022ProgramSetAuthorityInstruction(Instruction):
        authority_type: int
        new_authority: Account

        mint_account: Account
        current_authority: Account

    class Token2022ProgramMinttoInstruction(Instruction):
        amount: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class Token2022ProgramBurnInstruction(Instruction):
        amount: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class Token2022ProgramCloseAccountInstruction(Instruction):

        account_to_close: Account
        destination_account: Account
        owner: Account

    class Token2022ProgramFreezeAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class Token2022ProgramThawAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class Token2022ProgramTransferCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        destination_account: Account
        owner: Account

    class Token2022ProgramApproveCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        delegate: Account
        owner: Account

    class Token2022ProgramMinttoCheckedInstruction(Instruction):
        amount: int
        decimals: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class Token2022ProgramBurnCheckedInstruction(Instruction):
        amount: int
        decimals: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class Token2022ProgramInitializeAccount2Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account
        rent_sysvar: Account

    class Token2022ProgramSyncNativeInstruction(Instruction):

        token_account: Account

    class Token2022ProgramInitializeAccount3Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account

    class Token2022ProgramInitializeImmutableOwnerInstruction(Instruction):

        account_to_initialize: Account

    class AssociatedTokenAccountProgramCreateInstruction(Instruction):

        funding_account: Account
        associated_token_account: Account
        wallet_address: Account
        token_mint: Account
        system_program: Account
        spl_token: Account

    class AssociatedTokenAccountProgramCreateIdempotentInstruction(Instruction):

        funding_account: Account
        associated_token_account: Account
        wallet_address: Account
        token_mint: Account
        system_program: Account
        spl_token: Account

    class AssociatedTokenAccountProgramRecoverNestedInstruction(Instruction):

        nested_account: Account
        token_mint_nested: Account
        associated_token_account: Account
        owner: Account
        token_mint_owner: Account
        wallet_address: Account
        spl_token: Account

    class MemoProgramMemoInstruction(Instruction):
        memo: str

        signer_accounts: Account | None

    class MemoLegacyProgramMemoInstruction(Instruction):
        memo: str

        signer_accounts: Account | None


def get_instruction_id_length(program_id: str) -> InstructionIdFormat:
    if program_id == SYSTEM_PROGRAM_ID:
        return InstructionIdFormat(4, True)
    if program_id == STAKE_PROGRAM_ID:
        return InstructionIdFormat(4, True)
    if program_id == COMPUTE_BUDGET_PROGRAM_ID:
        return InstructionIdFormat(1, True)
    if program_id == TOKEN_PROGRAM_ID:
        return InstructionIdFormat(1, True)
    if program_id == TOKEN_2022_PROGRAM_ID:
        return InstructionIdFormat(1, True)
    if program_id == ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID:
        return InstructionIdFormat(1, False)
    if program_id == MEMO_PROGRAM_ID:
        return InstructionIdFormat(0, False)
    if program_id == MEMO_LEGACY_PROGRAM_ID:
        return InstructionIdFormat(0, False)

    return InstructionIdFormat(0, False)


def get_instruction(
    program_id: str,
    instruction_id: int,
    instruction_accounts: list[Account],
    instruction_data: bytes,
) -> Instruction:
    if program_id == SYSTEM_PROGRAM_ID:
        if instruction_id == SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT,
                [
                    PropertyTemplate(
                        "lamports",
                        "lamports",
                        False,
                    ),
                    PropertyTemplate(
                        "space",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "owner",
                        "authority",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "new_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "new_account",
                        "Create account",
                        False,
                    ),
                    UIProperty(
                        "lamports",
                        None,
                        "Deposit",
                        False,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "From",
                        False,
                    ),
                ],
                "System Program: Create Account",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_ASSIGN:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_ASSIGN,
                [
                    PropertyTemplate(
                        "owner",
                        "authority",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "assigned_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "assigned_account",
                        "Assigned account",
                        False,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "To program",
                        False,
                    ),
                ],
                "System Program: Assign",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_TRANSFER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_TRANSFER,
                [
                    PropertyTemplate(
                        "lamports",
                        "lamports",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Transfer",
                        False,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Sender",
                        False,
                    ),
                    UIProperty(
                        None,
                        "recipient_account",
                        "Recipient",
                        False,
                    ),
                ],
                "System Program: Transfer",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT_WITH_SEED,
                [
                    PropertyTemplate(
                        "base",
                        "pubkey",
                        False,
                    ),
                    PropertyTemplate(
                        "seed",
                        "string",
                        False,
                    ),
                    PropertyTemplate(
                        "lamports",
                        "lamports",
                        False,
                    ),
                    PropertyTemplate(
                        "space",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "created_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "created_account",
                        "Create account",
                        False,
                    ),
                    UIProperty(
                        "lamports",
                        None,
                        "Deposit",
                        False,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "From",
                        False,
                    ),
                ],
                "System Program: Create Account With Seed",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_ADVANCE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_ADVANCE_NONCE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recent_blockhashes_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "nonce_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Advance nonce",
                        False,
                    ),
                    UIProperty(
                        None,
                        "nonce_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "System Program: Advance nonce account",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_WITHDRAW_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_WITHDRAW_NONCE_ACCOUNT,
                [
                    PropertyTemplate(
                        "lamports",
                        "lamports",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recent_blockhashes_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "nonce_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Nonce withdraw",
                        False,
                    ),
                    UIProperty(
                        None,
                        "nonce_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "recipient_account",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "nonce_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "System Program: Withdraw nonce account",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_INITIALIZE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_INITIALIZE_NONCE_ACCOUNT,
                [
                    PropertyTemplate(
                        "nonce_authority",
                        "authority",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recent_blockhashes_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Initialize nonce account",
                        False,
                    ),
                    UIProperty(
                        "nonce_authority",
                        None,
                        "New authority",
                        False,
                    ),
                ],
                "System Program: Initialize nonce account",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_AUTHORIZE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_AUTHORIZE_NONCE_ACCOUNT,
                [
                    PropertyTemplate(
                        "nonce_authority",
                        "authority",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "nonce_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Set nonce authority",
                        False,
                    ),
                    UIProperty(
                        "nonce_authority",
                        None,
                        "New authority",
                        False,
                    ),
                    UIProperty(
                        None,
                        "nonce_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "System Program: Authorize nonce account",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_ALLOCATE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_ALLOCATE,
                [
                    PropertyTemplate(
                        "space",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "new_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "new_account",
                        "Allocate account",
                        False,
                    ),
                    UIProperty(
                        "space",
                        None,
                        "Data size",
                        False,
                    ),
                ],
                "System Program: Allocate",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_ALLOCATE_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_ALLOCATE_WITH_SEED,
                [
                    PropertyTemplate(
                        "base",
                        "pubkey",
                        False,
                    ),
                    PropertyTemplate(
                        "seed",
                        "string",
                        False,
                    ),
                    PropertyTemplate(
                        "space",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "allocated_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "allocated_account",
                        "Allocate account",
                        False,
                    ),
                    UIProperty(
                        "space",
                        None,
                        "Data size",
                        False,
                    ),
                ],
                "System Program: Allocate With Seed",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_ASSIGN_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_ASSIGN_WITH_SEED,
                [
                    PropertyTemplate(
                        "base",
                        "pubkey",
                        False,
                    ),
                    PropertyTemplate(
                        "seed",
                        "string",
                        False,
                    ),
                    PropertyTemplate(
                        "owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "assigned_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "assigned_account",
                        "Assigned account",
                        False,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "To program",
                        False,
                    ),
                ],
                "System Program: Assign With Seed",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_TRANSFER_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_TRANSFER_WITH_SEED,
                [
                    PropertyTemplate(
                        "lamports",
                        "lamports",
                        False,
                    ),
                    PropertyTemplate(
                        "from_seed",
                        "string",
                        False,
                    ),
                    PropertyTemplate(
                        "from_owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Transfer",
                        False,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Sender",
                        False,
                    ),
                    UIProperty(
                        None,
                        "recipient_account",
                        "Recipient",
                        False,
                    ),
                ],
                "System Program: Transfer With Seed",
                True,
                True,
                False,
                None,
            )
        if instruction_id == SYSTEM_PROGRAM_ID_INS_UPGRADE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                SYSTEM_PROGRAM_ID_INS_UPGRADE_NONCE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Upgrade nonce account",
                        False,
                    ),
                ],
                "System Program: Upgrade Nonce Account",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "System Program",
            True,
            False,
            False,
        )
    if program_id == STAKE_PROGRAM_ID:
        if instruction_id == STAKE_PROGRAM_ID_INS_INITIALIZE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_INITIALIZE,
                [
                    PropertyTemplate(
                        "staker",
                        "authority",
                        False,
                    ),
                    PropertyTemplate(
                        "withdrawer",
                        "authority",
                        False,
                    ),
                    PropertyTemplate(
                        "unix_timestamp",
                        "unix_timestamp",
                        False,
                    ),
                    PropertyTemplate(
                        "epoch",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "custodian",
                        "authority",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "uninitialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "uninitialized_stake_account",
                        "Initialize stake account",
                        False,
                    ),
                    UIProperty(
                        "staker",
                        None,
                        "New stake authority",
                        False,
                    ),
                    UIProperty(
                        "withdrawer",
                        None,
                        "New withdraw authority",
                        False,
                    ),
                    UIProperty(
                        "unix_timestamp",
                        None,
                        "Lockup time",
                        False,
                    ),
                    UIProperty(
                        "epoch",
                        None,
                        "Lockup epoch",
                        False,
                    ),
                    UIProperty(
                        "custodian",
                        None,
                        "Lockup authority",
                        False,
                    ),
                ],
                "Stake Program: Initialize",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_AUTHORIZE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_AUTHORIZE,
                [
                    PropertyTemplate(
                        "pubkey",
                        "pubkey",
                        False,
                    ),
                    PropertyTemplate(
                        "stake_authorize",
                        "StakeAuthorize",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set stake authority for",
                        False,
                    ),
                    UIProperty(
                        "pubkey",
                        None,
                        "New authority",
                        False,
                    ),
                    UIProperty(
                        "stake_authorize",
                        None,
                        "Authority type",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Authorized by",
                        False,
                    ),
                    UIProperty(
                        None,
                        "lockup_authority",
                        "Custodian",
                        False,
                    ),
                ],
                "Stake Program: Authorize",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_DELEGATE_STAKE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_DELEGATE_STAKE,
                [],
                [
                    AccountTemplate(
                        "initialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "vote_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_history_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "config_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "initialized_stake_account",
                        "Delegate from",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                    ),
                    UIProperty(
                        None,
                        "vote_account",
                        "Vote account",
                        False,
                    ),
                ],
                "Stake Program: Delegate Stake",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_SPLIT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_SPLIT,
                [
                    PropertyTemplate(
                        "lamports",
                        "lamports",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "uninitialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Split stake",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "uninitialized_stake_account",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "Stake Program: Split",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_WITHDRAW:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_WITHDRAW,
                [
                    PropertyTemplate(
                        "lamports",
                        "lamports",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_history_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "withdrawal_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Stake withdraw",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "recipient_account",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "withdrawal_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "Stake Program: Withdraw",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_DEACTIVATE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_DEACTIVATE,
                [],
                [
                    AccountTemplate(
                        "delegated_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegated_stake_account",
                        "Deactivate stake",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "Stake Program: Deactivate",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_SET_LOCKUP:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_SET_LOCKUP,
                [
                    PropertyTemplate(
                        "unix_timestamp",
                        "unix_timestamp",
                        True,
                    ),
                    PropertyTemplate(
                        "epoch",
                        "u64",
                        True,
                    ),
                    PropertyTemplate(
                        "custodian",
                        "pubkey",
                        True,
                    ),
                ],
                [
                    AccountTemplate(
                        "initialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_or_withdraw_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "initialized_stake_account",
                        None,
                        "Set lockup",
                        False,
                    ),
                    UIProperty(
                        "unix_timestamp",
                        None,
                        "Time",
                        False,
                    ),
                    UIProperty(
                        "epoch",
                        None,
                        "Epoch",
                        False,
                    ),
                    UIProperty(
                        None,
                        "custodian",
                        "New authority",
                        False,
                    ),
                    UIProperty(
                        None,
                        "lockup_or_withdraw_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "Stake Program: Set Lockup",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_MERGE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_MERGE,
                [],
                [
                    AccountTemplate(
                        "destination_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "source_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_history_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "source_stake_account",
                        "Merge",
                        False,
                    ),
                    UIProperty(
                        None,
                        "destination_stake_account",
                        "Into",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "Stake Program: Merge",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_AUTHORIZE_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_AUTHORIZE_WITH_SEED,
                [
                    PropertyTemplate(
                        "new_authorized_pubkey",
                        "pubkey",
                        False,
                    ),
                    PropertyTemplate(
                        "stake_authorize",
                        "StakeAuthorize",
                        False,
                    ),
                    PropertyTemplate(
                        "authority_seed",
                        "string",
                        False,
                    ),
                    PropertyTemplate(
                        "authority_owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set stake auth",
                        False,
                    ),
                    UIProperty(
                        "new_authorized_pubkey",
                        None,
                        "New (stake/withdraw) auth",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Authorized by",
                        False,
                    ),
                    UIProperty(
                        None,
                        "lockup_authority",
                        "Custodian",
                        False,
                    ),
                ],
                "Stake Program: Authorize With Seed",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_INITIALIZE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_INITIALIZE_CHECKED,
                [],
                [
                    AccountTemplate(
                        "uninitialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "withdrawal_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "uninitialized_stake_account",
                        "Uninitialized stake account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "New stake authority",
                        False,
                    ),
                    UIProperty(
                        None,
                        "withdrawal_authority",
                        "New withdraw authority",
                        False,
                    ),
                ],
                "Stake Program: Initialize Checked",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED,
                [
                    PropertyTemplate(
                        "stake_authorize",
                        "StakeAuthorize",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "new_stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set stake auth",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Stake or withdraw authority",
                        False,
                    ),
                    UIProperty(
                        None,
                        "new_stake_or_withdraw_authority",
                        "New stake or withdraw authority",
                        False,
                    ),
                ],
                "Stake Program: Authorize Checked",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED_WITH_SEED,
                [
                    PropertyTemplate(
                        "stake_authorize",
                        "StakeAuthorize",
                        False,
                    ),
                    PropertyTemplate(
                        "authority_seed",
                        "string",
                        False,
                    ),
                    PropertyTemplate(
                        "authority_owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "new_stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set stake account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "new_stake_or_withdraw_authority",
                        "New authority",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_authorize",
                        "Authority type",
                        False,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Authorized by",
                        False,
                    ),
                    UIProperty(
                        None,
                        "lockup_authority",
                        "Custodian",
                        False,
                    ),
                ],
                "Stake Program: Authorize Checked With Seed",
                True,
                True,
                False,
                None,
            )
        if instruction_id == STAKE_PROGRAM_ID_INS_SET_LOCKUP_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                STAKE_PROGRAM_ID_INS_SET_LOCKUP_CHECKED,
                [
                    PropertyTemplate(
                        "unix_timestamp",
                        "unix_timestamp",
                        True,
                    ),
                    PropertyTemplate(
                        "epoch",
                        "u64",
                        True,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "new_lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "initialized_stake_account",
                        "Set lockup",
                        False,
                    ),
                    UIProperty(
                        "unix_timestamp",
                        None,
                        "Time",
                        False,
                    ),
                    UIProperty(
                        "epoch",
                        None,
                        "Epoch",
                        False,
                    ),
                    UIProperty(
                        None,
                        "new_lockup_authority",
                        "New authority",
                        False,
                    ),
                    UIProperty(
                        None,
                        "lockup_or_withdraw_authority",
                        "Authorized by",
                        False,
                    ),
                ],
                "Stake Program: Set Lockup Checked",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Stake Program",
            True,
            False,
            False,
        )
    if program_id == COMPUTE_BUDGET_PROGRAM_ID:
        if instruction_id == COMPUTE_BUDGET_PROGRAM_ID_INS_REQUEST_HEAP_FRAME:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                COMPUTE_BUDGET_PROGRAM_ID_INS_REQUEST_HEAP_FRAME,
                [
                    PropertyTemplate(
                        "bytes",
                        "u32",
                        False,
                    ),
                ],
                [],
                [
                    UIProperty(
                        "bytes",
                        None,
                        "Bytes",
                        False,
                    ),
                ],
                "Compute Budget Program: Request Heap Frame",
                True,
                True,
                False,
                None,
            )
        if instruction_id == COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT,
                [
                    PropertyTemplate(
                        "units",
                        "u32",
                        False,
                    ),
                ],
                [],
                [
                    UIProperty(
                        "units",
                        None,
                        "Units",
                        False,
                    ),
                ],
                "Compute Budget Program: Set Compute Unit Limit",
                True,
                True,
                False,
                None,
            )
        if instruction_id == COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE,
                [
                    PropertyTemplate(
                        "lamports",
                        "u64",
                        False,
                    ),
                ],
                [],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Compute unit price",
                        False,
                    ),
                ],
                "Compute Budget Program: Set Compute Unit Price",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Compute Budget Program",
            True,
            False,
            False,
        )
    if program_id == TOKEN_PROGRAM_ID:
        if instruction_id == TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "Mint",
                        False,
                    ),
                ],
                "Token Program: Initialize Account",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_INITIALIZE_MULTISIG:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_INITIALIZE_MULTISIG,
                [
                    PropertyTemplate(
                        "number_of_signers",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "multisig_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "signer_accounts",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "multisig_account",
                        "Init multisig",
                        False,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Required signers",
                        False,
                    ),
                ],
                "Token Program: Initialize Multisig",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_TRANSFER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_TRANSFER,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Transfer tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Transfer",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_APPROVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_APPROVE,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegate_account",
                        "Approve delegate",
                        False,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Approve",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_REVOKE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_REVOKE,
                [],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "source_account",
                        "Rewoke delegate",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Revoke",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_SET_AUTHORITY:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_SET_AUTHORITY,
                [
                    PropertyTemplate(
                        "authority_type",
                        "AuthorityType",
                        False,
                    ),
                    PropertyTemplate(
                        "new_authority",
                        "authority",
                        True,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "current_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "mint_account",
                        "Set authority for",
                        False,
                    ),
                    UIProperty(
                        "new_authority",
                        None,
                        "New authority",
                        False,
                    ),
                    UIProperty(
                        "authority_type",
                        None,
                        "Authority type",
                        False,
                    ),
                    UIProperty(
                        None,
                        "current_authority",
                        "Current authority",
                        False,
                    ),
                ],
                "Token Program: Set Authority",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_MINT_TO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_MINT_TO,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Mint tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Mint authority",
                        False,
                    ),
                ],
                "Token Program: Mint to",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_BURN:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_BURN,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Burn tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Mint authority",
                        False,
                    ),
                ],
                "Token Program: Burn",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_CLOSE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_CLOSE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_close",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_close",
                        "Close account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "Withdraw to",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Close Account",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_FREEZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_FREEZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Freeze account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Freeze Account",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_THAW_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_THAW_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Thaw account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Thaw Account",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_TRANSFER_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_TRANSFER_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Transfer tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Transfer Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_APPROVE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_APPROVE_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegate",
                        "Approve delegate",
                        False,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Approve Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_MINT_TO_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_MINT_TO_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Mint tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Mint to Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_BURN_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_BURN_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Burn tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token Program: Burn Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2,
                [
                    PropertyTemplate(
                        "owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "Mint",
                        False,
                    ),
                ],
                "Token Program: Initialize Account 2",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_SYNC_NATIVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_SYNC_NATIVE,
                [],
                [
                    AccountTemplate(
                        "token_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_account",
                        "Sync native account",
                        False,
                    ),
                ],
                "Token Program: Sync Native",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3,
                [
                    PropertyTemplate(
                        "owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "Mint",
                        False,
                    ),
                ],
                "Token Program: Initialize Account 3",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                ],
                "Token Program: Initialize Immutable Owner",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Token Program",
            True,
            False,
            False,
        )
    if program_id == TOKEN_2022_PROGRAM_ID:
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "Mint",
                        False,
                    ),
                ],
                "Token 2022 Program: Initialize Account",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_MULTISIG:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_MULTISIG,
                [
                    PropertyTemplate(
                        "number_of_signers",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "multisig_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "signer_accounts",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "multisig_account",
                        "Init multisig",
                        False,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Required signers",
                        False,
                    ),
                ],
                "Token 2022 Program: Initialize Multisig",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_TRANSFER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_TRANSFER,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Transfer tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Transfer",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_APPROVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_APPROVE,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegate_account",
                        "Approve delegate",
                        False,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Approve",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_REVOKE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_REVOKE,
                [],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "source_account",
                        "Rewoke delegate",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Revoke",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_SET_AUTHORITY:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_SET_AUTHORITY,
                [
                    PropertyTemplate(
                        "authority_type",
                        "AuthorityType",
                        False,
                    ),
                    PropertyTemplate(
                        "new_authority",
                        "authority",
                        True,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "current_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "new_authority",
                        None,
                        "Set authority",
                        False,
                    ),
                    UIProperty(
                        "authority_type",
                        None,
                        "Type",
                        False,
                    ),
                    UIProperty(
                        "current_authority",
                        None,
                        "Type",
                        False,
                    ),
                    UIProperty(
                        "mint_account",
                        None,
                        "Token mint",
                        False,
                    ),
                ],
                "Token 2022 Program: Set Authority",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_MINT_TO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_MINT_TO,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Mint tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Mint authority",
                        False,
                    ),
                ],
                "Token 2022 Program: Mint to",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_BURN:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_BURN,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Burn tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Mint authority",
                        False,
                    ),
                ],
                "Token 2022 Program: Burn",
                True,
                True,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_CLOSE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_CLOSE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_close",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_close",
                        "Close account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "Withdraw to",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Close Account",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_FREEZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_FREEZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Freeze account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Freeze Account",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_THAW_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_THAW_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Thaw account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Thaw Account",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_TRANSFER_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_TRANSFER_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Transfer tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Transfer Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_APPROVE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_APPROVE_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegate",
                        "Approve delegate",
                        False,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Approve Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_MINT_TO_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_MINT_TO_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Mint tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Mint to Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_BURN_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_BURN_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        "u64",
                        False,
                    ),
                    PropertyTemplate(
                        "decimals",
                        "u8",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Burn tokens",
                        False,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                    ),
                ],
                "Token 2022 Program: Burn Checked",
                True,
                True,
                True,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2,
                [
                    PropertyTemplate(
                        "owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "Mint",
                        False,
                    ),
                ],
                "Token 2022 Program: Initialize Account 2",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_SYNC_NATIVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_SYNC_NATIVE,
                [],
                [
                    AccountTemplate(
                        "token_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_account",
                        "Sync native account",
                        False,
                    ),
                ],
                "Token 2022 Program: Sync Native",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3,
                [
                    PropertyTemplate(
                        "owner",
                        "pubkey",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "Mint",
                        False,
                    ),
                ],
                "Token 2022 Program: Initialize Account 3",
                True,
                True,
                False,
                None,
            )
        if instruction_id == TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                    ),
                ],
                "Token 2022 Program: Initialize Immutable Owner",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Token 2022 Program",
            True,
            False,
            False,
        )
    if program_id == ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID:
        if instruction_id == ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE,
                [],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "associated_token_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "wallet_address",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "system_program",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "spl_token",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "associated_token_account",
                        "Create token account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "token_mint",
                        "From mint",
                        False,
                    ),
                    UIProperty(
                        None,
                        "wallet_address",
                        "Owned by",
                        False,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Funded by",
                        False,
                    ),
                ],
                "Associated Token Account Program: Create",
                True,
                True,
                False,
                None,
            )
        if instruction_id == ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE_IDEMPOTENT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE_IDEMPOTENT,
                [],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "associated_token_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "wallet_address",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "system_program",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "spl_token",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "associated_token_account",
                        "Create token account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "token_mint",
                        "From mint",
                        False,
                    ),
                    UIProperty(
                        None,
                        "wallet_address",
                        "Owned by",
                        False,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Funded by",
                        False,
                    ),
                ],
                "Associated Token Account Program: Create Idempotent",
                True,
                True,
                False,
                None,
            )
        if instruction_id == ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_RECOVER_NESTED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_RECOVER_NESTED,
                [],
                [
                    AccountTemplate(
                        "nested_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint_nested",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "associated_token_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint_owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "wallet_address",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "spl_token",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nested_account",
                        "Recover nested token account",
                        False,
                    ),
                    UIProperty(
                        None,
                        "associated_token_account",
                        "Transfer recovered tokens to",
                        False,
                    ),
                    UIProperty(
                        None,
                        "wallet_address",
                        "Transfer recovered SOL to",
                        False,
                    ),
                ],
                "Associated Token Account Program: Recover Nested",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Associated Token Account Program",
            True,
            False,
            False,
        )
    if program_id == MEMO_PROGRAM_ID:
        if instruction_id == MEMO_PROGRAM_ID_INS_MEMO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                MEMO_PROGRAM_ID_INS_MEMO,
                [
                    PropertyTemplate(
                        "memo",
                        "memo",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "signer_accounts",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        "memo",
                        None,
                        "Memo",
                        False,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Signer accounts",
                        False,
                    ),
                ],
                "Memo Program: Memo",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Memo Program",
            True,
            False,
            False,
        )
    if program_id == MEMO_LEGACY_PROGRAM_ID:
        if instruction_id == MEMO_LEGACY_PROGRAM_ID_INS_MEMO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                MEMO_LEGACY_PROGRAM_ID_INS_MEMO,
                [
                    PropertyTemplate(
                        "memo",
                        "memo",
                        False,
                    ),
                ],
                [
                    AccountTemplate(
                        "signer_accounts",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        "memo",
                        None,
                        "Memo",
                        False,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Signer accounts",
                        False,
                    ),
                ],
                "Memo Legacy Program: Memo",
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Memo Legacy Program",
            True,
            False,
            False,
        )
    return Instruction(
        instruction_data,
        program_id,
        instruction_accounts,
        0,
        [],
        [],
        [],
        "Unsupported program",
        False,
        False,
        False,
    )


class StakeAuthorize:
    @classmethod
    def type(cls) -> str:
        return "u32"

    @classmethod
    def from_int(cls, value: int) -> str:
        if value == 0:
            return "Stake"
        if value == 1:
            return "Withdraw"
        raise DataError(f"Unknown value: {value}")


class AuthorityType:
    @classmethod
    def type(cls) -> str:
        return "u8"

    @classmethod
    def from_int(cls, value: int) -> str:
        if value == 0:
            return "Mint tokens"
        if value == 1:
            return "Freeze account"
        if value == 2:
            return "Account owner"
        if value == 3:
            return "Close account"
        raise DataError(f"Unknown value: {value}")


def enum_type_to_class(enum_type: str):
    if enum_type == "StakeAuthorize":
        return StakeAuthorize
    if enum_type == "AuthorityType":
        return AuthorityType
    raise DataError(f"Unknown enum type: {enum_type}")