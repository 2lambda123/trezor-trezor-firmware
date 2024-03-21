use crate::{
    error,
    strutil::TString,
    time::{Duration, Instant},
    ui::{
        animation::Animation,
        component::{
            base::ComponentExt,
            image::BlendedImage,
            text::{
                paragraphs::{Paragraph, ParagraphVecShort, Paragraphs},
                TextStyle,
            },
            Component, Empty, Event, EventCtx, Paginate, Qr, Timeout,
        },
        geometry::{Axis, Offset, Rect},
        layout::util::ConfirmBlob,
        model_mercury::{
            component::{Button, ButtonMsg, CancelConfirmMsg, CancelInfoConfirmMsg},
            constant,
        },
        shape::Renderer,
    },
};

use crate::micropython::buffer::StrBuffer;

use super::{
    theme, Frame, FrameMsg, IconDialog, Swipe, SwipeDirection, VerticalMenu, VerticalMenuChoiceMsg,
};

// TODO
// intra-component swipe
// generalize
// component storage @ micropython

const ANIMATION_DURATION: Duration = Duration::from_millis(600);


#[derive(Copy, Clone, PartialEq, Eq)]
enum State {
    Address,
    Menu,
    QrCode,
    AccountInfo,
    Cancel,
    Success,
}

#[derive(Copy, Clone)]
enum Decision {
    Nothing,
    Goto(State, SwipeDirection),
    Return(CancelConfirmMsg),
}

impl From<Option<(State, SwipeDirection)>> for Decision {
    fn from(val: Option<(State, SwipeDirection)>) -> Self {
        match val {
            Some((state, direction)) => Decision::Goto(state, direction),
            None => Decision::Nothing,
        }
    }
}

pub struct GetAddressFlow {
    state: State,
    transition: Option<Transition>,
    swipe: Swipe,
    c_address: Frame<SwipeScroller<Paragraphs<Paragraph<StrBuffer>>>, &'static str>,
    c_menu: Frame<VerticalMenu<&'static str>, &'static str>,
    c_qr: Frame<Qr, &'static str>,
    c_account_info: Frame<Paragraphs<ParagraphVecShort<StrBuffer>>, &'static str>,
    c_cancel: Frame<Paragraphs<Paragraph<StrBuffer>>, &'static str>,
    c_success: IconDialog<StrBuffer, Timeout>,

    a_copy: Option<Frame<SwipeScroller<Paragraphs<Paragraph<StrBuffer>>>, &'static str>>,
}

struct Transition {
    state: State,
    animation: Animation<Offset>,
    direction: SwipeDirection,
}

impl GetAddressFlow {
    pub fn new() -> Result<Self, error::Error> {
        // TODO parameters
        Ok(Self {
            state: State::Address,
            transition: None,
            c_address: Frame::left_aligned(
                "Receive",
                SwipeScroller::vertical(Paragraphs::new(Paragraph::new(
                    &theme::TEXT_MONO,
                    StrBuffer::from("https://youtu.be/iFkEs4GNgfc?si=Jl4UZSIAYGVcLQKohttps://youtu.be/iFkEs4GNgfc?si=Jl4UZSIAYGVcLQKohttps://youtu.be/iFkEs4GNgfc?si=Jl4UZSIAYGVcLQKohttps://youtu.be/iFkEs4GNgfc?si=Jl4UZSIAYGVcLQKohttps://youtu.be/iFkEs4GNgfc?si=Jl4UZSIAYGVcLQKo"),
                ))),
            )
            .with_subtitle("address")
            .with_info_button(),
            c_menu: Frame::left_aligned(
                "",
                VerticalMenu::context_menu([
                    ("Address QR code".into(), theme::ICON_QR_CODE),
                    ("Account info".into(), theme::ICON_CHEVRON_RIGHT),
                    ("Cancel transaction".into(), theme::ICON_CANCEL),
                ]),
            )
            .with_cancel_button(),
            c_qr: Frame::left_aligned(
                "Receive address",
                Qr::new("https://youtu.be/iFkEs4GNgfc?si=Jl4UZSIAYGVcLQKo", true)?,
            )
            .with_cancel_button(),
            c_account_info: Frame::left_aligned(
                "Account info",
                Paragraphs::new(ParagraphVecShort::new()),
            )
            .with_cancel_button(),
            c_cancel: Frame::left_aligned(
                "Cancel receive",
                Paragraphs::new(Paragraph::new(
                    &theme::TEXT_NORMAL,
                    StrBuffer::from("O rly?"),
                )),
            )
            .with_cancel_button(),
            c_success: IconDialog::new(
                BlendedImage::new(
                    theme::IMAGE_BG_CIRCLE,
                    theme::IMAGE_FG_WARN,
                    theme::SUCCESS_COLOR,
                    theme::FG,
                    theme::BG,
                ),
                StrBuffer::from("Confirmed"),
                Timeout::new(100),
            ),
            swipe: Swipe::new().down().up().left().right(),
            a_copy: None,
        })
    }

    fn goto(&mut self, ctx: &mut EventCtx, direction: SwipeDirection, state: State) {
        self.transition = Some(Transition {
            state,
            animation: Animation::new(
                Offset::zero(),
                Self::transition_offset(direction),
                ANIMATION_DURATION,
                Instant::now(),
            ),
            direction,
        });
        ctx.request_anim_frame();
        ctx.request_paint()
    }

    fn transition_offset(direction: SwipeDirection) -> Offset {
        match direction {
            SwipeDirection::Up => Offset::y(-constant::HEIGHT),
            SwipeDirection::Down => Offset::y(constant::HEIGHT),
            SwipeDirection::Left => Offset::x(-constant::WIDTH),
            SwipeDirection::Right => Offset::x(constant::WIDTH),
        }
    }

    // lookup + render
    fn render_state<'s>(&'s self, state: State, target: &mut impl Renderer<'s>) {
        match state {
            State::Address => self.c_address.render(target),
            State::Menu => self.c_menu.render(target),
            State::QrCode => self.c_qr.render(target),
            State::AccountInfo => self.c_account_info.render(target),
            State::Cancel => self.c_cancel.render(target),
            State::Success => self.c_success.render(target),
        }
    }

    // render, incl. temporary
    fn render_transition<'s>(&'s self, transition: &Transition, target: &mut impl Renderer<'s>) {
        let off = transition.animation.value(Instant::now());

        target.with_origin(off, &|target| {
            self.render_state(self.state, target);
        });
        if self.a_copy.is_some() {
            target.with_origin(off, &|target| {
                self.a_copy.render(target);
            });
            target.with_origin(
                off - Self::transition_offset(transition.direction),
                &|target| {
                    self.render_state(self.state, target);
                },
            );
        } else {
            target.with_origin(off, &|target| {
                self.render_state(self.state, target);
            });
            target.with_origin(
                off - Self::transition_offset(transition.direction),
                &|target| {
                    self.render_state(transition.state, target); //FIXME make transition.state the _old_ state
                },
            );
        }
    }

    // perhaps send attach event if transition finished
    fn handle_transition(&mut self, ctx: &mut EventCtx) {
        if let Some(transition) = &self.transition {
            if transition.animation.finished(Instant::now()) {
                self.state = transition.state;
                self.transition = None;
                self.a_copy = None;

                //FIXME
                if matches!(self.state, State::Success) {
                    self.c_success.event(ctx, Event::Attach);
                }
            } else {
                ctx.request_anim_frame();
            }
            ctx.request_paint();
        }
    }

    // lookup, handle swiping
    fn handle_swipe_child(&mut self, ctx: &mut EventCtx, direction: SwipeDirection) -> bool {
        match self.state {
            State::Address if self.c_address.can_swipe(direction) => {
                self.a_copy = Some(self.c_address.clone());
                self.c_address.swiped(ctx, direction);
                true
            }
            _ => false,
        }
    }

    fn handle_swipe(&self, ctx: &mut EventCtx, direction: SwipeDirection) -> Decision {
        // TODO can component handle it or do we switch between components?
        // either passthru
        // or change component
        match (&self.state, direction) {
            (State::Address, SwipeDirection::Left) => Decision::Goto(State::Menu, direction),
            (State::Address, SwipeDirection::Up) => Decision::Goto(State::Success, direction),
            (State::Menu, SwipeDirection::Right) => Decision::Goto(State::Address, direction),
            (State::QrCode, SwipeDirection::Right) => Decision::Goto(State::Menu, direction),
            (State::AccountInfo, SwipeDirection::Right) => Decision::Goto(State::Menu, direction),
            (State::Cancel, SwipeDirection::Up) => Decision::Return(CancelConfirmMsg::Cancelled),
            _ => Decision::Nothing,
        }
    }

    // lookup, handle event, convert message to action
    fn handle_child(&mut self, ctx: &mut EventCtx, event: Event) -> Decision {
        match self.state {
            State::Address => {
                if let Some(FrameMsg::Button(_)) = self.c_address.event(ctx, event) {
                    return Decision::Goto(State::Menu, SwipeDirection::Left);
                }
            }
            State::Menu => {
                return match self.c_menu.event(ctx, event) {
                    Some(FrameMsg::Content(VerticalMenuChoiceMsg::Selected(0))) => {
                        Decision::Goto(State::QrCode, SwipeDirection::Left)
                    }
                    Some(FrameMsg::Content(VerticalMenuChoiceMsg::Selected(1))) => {
                        Decision::Goto(State::AccountInfo, SwipeDirection::Left)
                    }
                    Some(FrameMsg::Content(VerticalMenuChoiceMsg::Selected(2))) => {
                        Decision::Goto(State::Cancel, SwipeDirection::Left)
                    }
                    Some(FrameMsg::Button(_)) => {
                        Decision::Goto(State::Address, SwipeDirection::Right)
                    }
                    None => Decision::Nothing,
                    _ => panic!(),
                }
            }
            State::QrCode => {
                if let Some(FrameMsg::Button(_)) = self.c_qr.event(ctx, event) {
                    return Decision::Goto(State::Menu, SwipeDirection::Right);
                }
            }
            State::AccountInfo => {
                if let Some(FrameMsg::Button(_)) = self.c_account_info.event(ctx, event) {
                    return Decision::Goto(State::Menu, SwipeDirection::Right);
                }
            }
            State::Cancel => {
                if let Some(FrameMsg::Button(_)) = self.c_cancel.event(ctx, event) {
                    return Decision::Goto(State::Menu, SwipeDirection::Right);
                }
            }
            State::Success => {
                if let Some(_) = self.c_success.event(ctx, event) {
                    return Decision::Return(CancelConfirmMsg::Confirmed);
                }
            }
        }
        return Decision::Nothing;
    }
}

impl Component for GetAddressFlow {
    type Msg = CancelConfirmMsg;

    // iterate + place
    fn place(&mut self, bounds: Rect) -> Rect {
        self.swipe.place(bounds);
        let b1 = self.c_address.place(bounds);
        let b2 = self.c_menu.place(bounds);
        let b3 = self.c_qr.place(bounds);
        let b4 = self.c_account_info.place(bounds);
        let b5 = self.c_cancel.place(bounds);
        let b6 = self.c_success.place(bounds);
        b1.union(b2).union(b3).union(b4).union(b5).union(b6)
    }

    fn event(&mut self, ctx: &mut EventCtx, event: Event) -> Option<Self::Msg> {
        // FIXME might want to send some events to all, e.g. Attach/Timer
        if let Event::Timer(EventCtx::ANIM_FRAME_TIMER) = event {
            self.handle_transition(ctx);
            return None;
        }
        let mut decision = Decision::Nothing;
        if let Some(direction) = self.swipe.event(ctx, event) {
            if self.handle_swipe_child(ctx, direction) {
                decision = Decision::Goto(self.state, direction)
                //XXX special case intra component paging
            } else {
                decision = self.handle_swipe(ctx, direction)
            }
        }
        if matches!(decision, Decision::Nothing) {
            decision = self.handle_child(ctx, event);
        }
        match decision {
            Decision::Nothing => None,
            Decision::Goto(next_state, direction) => {
                self.goto(ctx, direction, next_state);
                None
            }
            Decision::Return(msg) => Some(msg),
        }
    }

    fn paint(&mut self) {}

    fn render<'s>(&'s self, target: &mut impl Renderer<'s>) {
        if let Some(transition) = &self.transition {
            self.render_transition(transition, target)
        } else {
            self.render_state(self.state, target)
        }
    }
}

// trace
#[cfg(feature = "ui_debug")]
impl crate::trace::Trace for GetAddressFlow {
    fn trace(&self, t: &mut dyn crate::trace::Tracer) {
        /*
        t.component("IconDialog");
        t.child("image", &self.image);
        t.child("content", &self.paragraphs);
        t.child("controls", &self.controls);
        */
    }
}

trait Swipable {
    fn can_swipe(&self, direction: SwipeDirection) -> bool {
        false
    }

    fn swiped(&mut self, ctx: &mut EventCtx, direction: SwipeDirection) {}
}

impl Swipable for Qr {}

impl<T, U> Swipable for Frame<T, U>
where
    T: Component + Swipable,
    U: AsRef<str>,
{
    fn can_swipe(&self, direction: SwipeDirection) -> bool {
        self.inner().can_swipe(direction)
    }

    fn swiped(&mut self, ctx: &mut EventCtx, direction: SwipeDirection) {
        self.update_content(ctx, |ctx, inner| inner.swiped(ctx, direction))
    }
}

#[derive(Clone)]
struct SwipeScroller<T> {
    inner: T,
    axis: Axis,
    pages: usize,
    current: usize,
}

impl<T> SwipeScroller<T> {
    pub fn vertical(inner: T) -> Self {
        Self {
            inner,
            axis: Axis::Vertical,
            pages: 1,
            current: 0,
        }
    }
}

impl<T: Component + Paginate> Component for SwipeScroller<T> {
    type Msg = T::Msg;

    fn place(&mut self, bounds: Rect) -> Rect {
        let result = self.inner.place(bounds);
        self.pages = self.inner.page_count();
        result
    }

    fn event(&mut self, ctx: &mut EventCtx, event: Event) -> Option<Self::Msg> {
        let msg = self.inner.event(ctx, event);
        //self.pages = self.inner.page_count();
        msg
    }

    fn paint(&mut self) {
        self.inner.paint()
    }

    fn render<'s>(&'s self, target: &mut impl Renderer<'s>) {
        self.inner.render(target)
    }
}

impl<T: Component + Paginate> Swipable for SwipeScroller<T> {
    fn can_swipe(&self, direction: SwipeDirection) -> bool {
        match (self.axis, direction) {
            (Axis::Horizontal, SwipeDirection::Up | SwipeDirection::Down) => false,
            (Axis::Vertical, SwipeDirection::Left | SwipeDirection::Right) => false,
            (_, SwipeDirection::Left | SwipeDirection::Up) => self.current + 1 < self.pages,
            (_, SwipeDirection::Right | SwipeDirection::Down) => self.current > 0,
        }
    }

    fn swiped(&mut self, ctx: &mut EventCtx, direction: SwipeDirection) {
        match (self.axis, direction) {
            (Axis::Horizontal, SwipeDirection::Up | SwipeDirection::Down) => return,
            (Axis::Vertical, SwipeDirection::Left | SwipeDirection::Right) => return,
            (_, SwipeDirection::Left | SwipeDirection::Up) => {
                self.current = (self.current + 1).min(self.pages - 1);
                self.inner.change_page(self.current);
            }
            (_, SwipeDirection::Right | SwipeDirection::Down) => {
                self.current = self.current.saturating_sub(1);
                self.inner.change_page(self.current);
            }
        }
    }
}

macro_rules! dump_size {
    ($x:ty $(,)?) => {
        const size: usize = core::mem::size_of::<$x>();
        #[allow(unknown_lints, eq_op)]
        const _: [(); 0 - size] = [];
    };
}

dump_size!(GetAddressFlow);
