from .channel_context import ChannelContext
from . import ChannelState


def getPacketHandler(
    channel: ChannelContext, packet: bytes
):  # TODO is the packet bytes or BufferType?
    if channel.get_management_session_state is ChannelState.TH1:  # TODO is correct
        return handler_TH_1


def handler_TH_1(packet):
    pass
