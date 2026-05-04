---
title: "Gestures (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgestures"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Gestures

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.gestures.Gestures
------------------------------------------------------------------------
public final class Gestures extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Use this class to process touch events from the platform and detect gesture induced actions on the map view. Please note that this class holds strong references to the gesture listeners. On Android Auto, processing touch events is not needed. Instead, gestures get detected by android auto platform and provided via callbacks. For more information see onClick, onFling and onScale methods in <https://developer.android.com/reference/androidx/car/app/SurfaceCallback>.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [disableDefaultAction](#disableDefaultAction(com.here.sdk.gestures.GestureType))`(`[`GestureType`](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")` gestureType)`

Disables default action for a specified gesture.

`void`

  [enableDefaultAction](#enableDefaultAction(com.here.sdk.gestures.GestureType))`(`[`GestureType`](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")` gestureType)`

Enables default action to be performed for a specified gesture.

[`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures")

  [getDoubleTapListener](#getDoubleTapListener())`()`

Gets a [`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs.

[`FlingHandler`](sdk-for-android-explore-api-reference-latestflinghandler "class in com.here.sdk.gestures")

  [getFlingHandler](#getFlingHandler())`()`

Returns fling handler.

[`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures")

  [getLongPressListener](#getLongPressListener())`()`

Gets a [`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs.

[`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures")

  [getPanListener](#getPanListener())`()`

Gets a [`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs.

[`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures")

  [getPinchRotateListener](#getPinchRotateListener())`()`

Gets a [`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs.

[`ScaleHandler`](sdk-for-android-explore-api-reference-latestscalehandler "class in com.here.sdk.gestures")

  [getScaleHandler](#getScaleHandler())`()`

Returns scale handler.

[`ScrollHandler`](sdk-for-android-explore-api-reference-latestscrollhandler "class in com.here.sdk.gestures")

  [getScrollHandler](#getScrollHandler())`()`

Returns scroll handler.

[`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures")

  [getTapListener](#getTapListener())`()`

Gets a [`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs.

[`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures")

  [getTwoFingerPanListener](#getTwoFingerPanListener())`()`

Gets a [`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs.

[`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures")

  [getTwoFingerTapListener](#getTwoFingerTapListener())`()`

Gets a [`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs.

`void`

  [setDoubleTapListener](#setDoubleTapListener(com.here.sdk.gestures.DoubleTapListener))`(`[`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures")` value)`

Sets a [`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs.

`void`

  [setLongPressListener](#setLongPressListener(com.here.sdk.gestures.LongPressListener))`(`[`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures")` value)`

Sets a [`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs.

`void`

  [setPanListener](#setPanListener(com.here.sdk.gestures.PanListener))`(`[`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures")` value)`

Sets a [`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs.

`void`

  [setPinchRotateListener](#setPinchRotateListener(com.here.sdk.gestures.PinchRotateListener))`(`[`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures")` value)`

Sets a [`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs.

`void`

  [setTapListener](#setTapListener(com.here.sdk.gestures.TapListener))`(`[`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures")` value)`

Sets a [`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs.

`void`

  [setTwoFingerPanListener](#setTwoFingerPanListener(com.here.sdk.gestures.TwoFingerPanListener))`(`[`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures")` value)`

Sets a [`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs.

`void`

  [setTwoFingerTapListener](#setTwoFingerTapListener(com.here.sdk.gestures.TwoFingerTapListener))`(`[`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures")` value)`

Sets a [`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### enableDefaultAction

public void enableDefaultAction(@NonNull [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") gestureType)

    Enables default action to be performed for a specified gesture.
Parameters:
    `gestureType` -

    The gesture type.

### disableDefaultAction

public void disableDefaultAction(@NonNull [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") gestureType)

    Disables default action for a specified gesture.
Parameters:
    `gestureType` -

    The gesture type.

### getTapListener

@Nullable public [TapListener](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") getTapListener()

    Gets a [`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs. [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") holds a strong reference to the listener.
Returns:
    [`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs.

### setTapListener

public void setTapListener(@Nullable [TapListener](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") value)

    Sets a [`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs.
Parameters:
    `value` -

    [`TapListener`](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs.

### getDoubleTapListener

@Nullable public [DoubleTapListener](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") getDoubleTapListener()

    Gets a [`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs. [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") holds a strong reference to the listener.
Returns:
    [`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs.

### setDoubleTapListener

public void setDoubleTapListener(@Nullable [DoubleTapListener](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") value)

    Sets a [`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs.
Parameters:
    `value` -

    [`DoubleTapListener`](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs.

### getPinchRotateListener

@Nullable public [PinchRotateListener](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") getPinchRotateListener()

    Gets a [`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs. [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") holds a strong reference to the listener.
Returns:
    [`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs.

### setPinchRotateListener

public void setPinchRotateListener(@Nullable [PinchRotateListener](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") value)

    Sets a [`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs.
Parameters:
    `value` -

    [`PinchRotateListener`](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs.

### getLongPressListener

@Nullable public [LongPressListener](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") getLongPressListener()

    Gets a [`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs. [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") holds a strong reference to the listener.
Returns:
    [`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs.

### setLongPressListener

public void setLongPressListener(@Nullable [LongPressListener](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") value)

    Sets a [`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs.
Parameters:
    `value` -

    [`LongPressListener`](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs.

### getPanListener

@Nullable public [PanListener](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") getPanListener()

    Gets a [`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs. [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") holds a strong reference to the listener.
Returns:
    [`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs.

### setPanListener

public void setPanListener(@Nullable [PanListener](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") value)

    Sets a [`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs.
Parameters:
    `value` -

    [`PanListener`](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs.

### getTwoFingerTapListener

@Nullable public [TwoFingerTapListener](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") getTwoFingerTapListener()

    Gets a [`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs. [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") holds a strong reference to the listener.
Returns:
    [`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs.

### setTwoFingerTapListener

public void setTwoFingerTapListener(@Nullable [TwoFingerTapListener](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") value)

    Sets a [`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs.
Parameters:
    `value` -

    [`TwoFingerTapListener`](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs.

### getTwoFingerPanListener

@Nullable public [TwoFingerPanListener](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") getTwoFingerPanListener()

    Gets a [`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs. [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") holds a strong reference to the listener.
Returns:
    [`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs.

### setTwoFingerPanListener

public void setTwoFingerPanListener(@Nullable [TwoFingerPanListener](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") value)

    Sets a [`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs.
Parameters:
    `value` -

    [`TwoFingerPanListener`](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs.

### getScrollHandler

@NonNull public [ScrollHandler](sdk-for-android-explore-api-reference-latestscrollhandler "class in com.here.sdk.gestures") getScrollHandler()

    Returns scroll handler. See [`ScrollHandler.onScroll(float, float)`](sdk-for-android-explore-api-reference-latestscrollhandler#onScroll(float,float)) for more details.
Returns:
    Scroll handler.

### getScaleHandler

@NonNull public [ScaleHandler](sdk-for-android-explore-api-reference-latestscalehandler "class in com.here.sdk.gestures") getScaleHandler()

    Returns scale handler. See [`ScaleHandler.onScale(float, float, float)`](sdk-for-android-explore-api-reference-latestscalehandler#onScale(float,float,float)) for more details.
Returns:
    Scale handler.

### getFlingHandler

@NonNull public [FlingHandler](sdk-for-android-explore-api-reference-latestflinghandler "class in com.here.sdk.gestures") getFlingHandler()

    Returns fling handler. See [`FlingHandler.onFling(float, float)`](sdk-for-android-explore-api-reference-latestflinghandler#onFling(float,float)) for more details.
Returns:
    Fling handler.
