from typing import TYPE_CHECKING

from trezor.utils import BufferReader
from trezor.wire import ProcessError

from .parse import parse_property

if TYPE_CHECKING:
    from typing import Any, TypeGuard, ClassVar

    from ..types import Account, AccountTemplate, PropertyTemplate, UIProperty


class Instruction:
    PROGRAM_ID: ClassVar[str]
    INSTRUCTION_ID: ClassVar[int]

    program_id: str
    instruction_id: int

    property_templates: list[PropertyTemplate]
    accounts_template: list[AccountTemplate]

    ui_name: str

    ui_properties: list[UIProperty]

    parsed_data: dict[str, Any] | None = None
    parsed_accounts: dict[str, Account] | None = None

    is_program_supported: bool
    is_instruction_supported: bool
    instruction_data: bytes | None = None
    accounts: list[Account] | None = None

    is_multisig: bool = False
    multisig_signers: list[Account] | None = None

    is_deprecated_warning: str | None = None

    def __init__(
        self,
        instruction_data: bytes,
        program_id: str,
        accounts: list[Account],
        instruction_id: int,
        property_templates: list[PropertyTemplate],
        accounts_template: list[AccountTemplate],
        ui_properties: list[UIProperty],
        ui_name: str,
        is_program_supported: bool = True,
        is_instruction_supported: bool = True,
        supports_multisig: bool = False,
        is_deprecated_warning: str | None = None,
    ) -> None:
        self.program_id = program_id
        self.instruction_id = instruction_id

        self.property_templates = property_templates
        self.accounts_template = accounts_template

        self.ui_name = ui_name

        self.ui_properties = ui_properties

        self.parsed_data = {}
        self.parsed_accounts = {}

        self.is_program_supported = is_program_supported
        self.is_instruction_supported = is_instruction_supported

        self.is_deprecated_warning = is_deprecated_warning

        self.instruction_data = instruction_data
        self.accounts = accounts

        reader = BufferReader(instruction_data)
        
        parsed_data = {}
        for property_template in property_templates:
            property = parse_property(
                reader, property_template.type, property_template.optional
            )
            
            parsed_data[property_template.name] = property
        self.parsed_data = parsed_data

        
        parsed_account = {}
        for i, account_template in enumerate(accounts_template):
            if i >= len(accounts):
                if account_template.optional:
                    continue
                else:
                    raise ValueError(f"Account {account_template.name} is missing")

            parsed_account[account_template.name] = accounts[i]
        self.parsed_accounts = parsed_account


        if supports_multisig and len(accounts) > len(accounts_template):
            self.is_multisig = True
            self.multisig_signers = accounts[len(accounts_template) :]

        if reader.remaining_count() != 0:
            raise ProcessError("Invalid transaction")

    def __getattr__(self, attr: str) -> Any:
        assert self.parsed_data is not None
        assert self.parsed_accounts is not None

        if attr in self.parsed_data:
            return self.parsed_data[attr]
        if attr in self.parsed_accounts:
            return self.parsed_accounts[attr]

        raise AttributeError(f"Attribute {attr} not found")

    def get_property_template(self, property: str) -> PropertyTemplate:
        for property_template in self.property_templates:
            if property_template.name == property:
                return property_template

        raise ValueError(f"Property {property} not found")

    def get_account_template(self, account_name: str) -> AccountTemplate:
        for account_template in self.accounts_template:
            if account_template.name == account_name:
                return account_template

        raise ValueError(f"Account {account_name} not found")

    @classmethod
    def is_type_of(cls, ins: Any) -> TypeGuard["Instruction"]:
        return (
            ins.program_id == cls.PROGRAM_ID
            and ins.instruction_id == cls.INSTRUCTION_ID
        )
