---
title: "Gestures (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-gestures"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.gestures](sdk-for-android-explore-com-here-sdk-gestures-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.gestures.Gestures → com.here.NativeBase com.here.sdk.gestures.Gestures → com.here.sdk.gestures.Gestures

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">Gestures</span> <span class="extends-implements">extends [NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Use this class to process touch events from the platform and detect gesture induced actions on the map view. Please note that this class holds strong references to the gesture listeners. On Android Auto, processing touch events is not needed. Instead, gestures get detected by android auto platform and provided via callbacks. For more information see onClick, onFling and onScale methods in https://developer.android.com/reference/androidx/car/app/SurfaceCallback .

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      disableDefaultAction ( GestureType gestureType)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Disables default action for a specified gesture.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      enableDefaultAction ( GestureType gestureType)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Enables default action to be performed for a specified gesture.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`DoubleTapListener`](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDoubleTapListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a DoubleTapListener that notifies when a double-tap gesture occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`FlingHandler`](sdk-for-android-explore-com-here-sdk-gestures-flinghandler "class in com.here.sdk.gestures")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFlingHandler ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns fling handler.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LongPressListener`](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLongPressListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a LongPressListener that notifies when a long-press gesture occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`PanListener`](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPanListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a PanListener that notifies when a pan gesture occurs.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`PinchRotateListener`](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPinchRotateListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a PinchRotateListener that notifies when a pinch-rotate gesture occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`ScaleHandler`](sdk-for-android-explore-com-here-sdk-gestures-scalehandler "class in com.here.sdk.gestures")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getScaleHandler ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns scale handler.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`ScrollHandler`](sdk-for-android-explore-com-here-sdk-gestures-scrollhandler "class in com.here.sdk.gestures")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getScrollHandler ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns scroll handler.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TapListener`](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTapListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a TapListener that notifies when a tap gesture occurs.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TwoFingerPanListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTwoFingerPanListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a TwoFingerPanListener that notifies when a two-finger pan gesture occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TwoFingerTapListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTwoFingerTapListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a TwoFingerTapListener that notifies when a two-finger tap gesture occurs.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDoubleTapListener ( DoubleTapListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a DoubleTapListener that notifies when a double-tap gesture occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setLongPressListener ( LongPressListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a LongPressListener that notifies when a long-press gesture occurs.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPanListener ( PanListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a PanListener that notifies when a pan gesture occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPinchRotateListener ( PinchRotateListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a PinchRotateListener that notifies when a pinch-rotate gesture occurs.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTapListener ( TapListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a TapListener that notifies when a tap gesture occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTwoFingerPanListener ( TwoFingerPanListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a TwoFingerPanListener that notifies when a two-finger pan gesture occurs.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTwoFingerTapListener ( TwoFingerTapListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a TwoFingerTapListener that notifies when a two-finger tap gesture occurs.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-enableDefaultAction-com-here-sdk-gestures-GestureType" class="section detail">

    ### enableDefaultAction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableDefaultAction</span><wbr></wbr><span class="parameters">(@NonNull [GestureType](sdk-for-android-explore-com-here-sdk-gestures-gesturetype "enum class in com.here.sdk.gestures") gestureType)</span>

    </div>

    <div class="block">

    Enables default action to be performed for a specified gesture.

    </div>

    Parameters:  
    `gestureType` -

    The gesture type.

    </div>

  - <div id="sdk-for-android-explore-disableDefaultAction-com-here-sdk-gestures-GestureType" class="section detail">

    ### disableDefaultAction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disableDefaultAction</span><wbr></wbr><span class="parameters">(@NonNull [GestureType](sdk-for-android-explore-com-here-sdk-gestures-gesturetype "enum class in com.here.sdk.gestures") gestureType)</span>

    </div>

    <div class="block">

    Disables default action for a specified gesture.

    </div>

    Parameters:  
    `gestureType` -

    The gesture type.

    </div>

  - <div id="sdk-for-android-explore-getTapListener" class="section detail">

    ### getTapListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[TapListener](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getTapListener</span>()

    </div>

    <div class="block">

    Gets a TapListener that notifies when a tap gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`TapListener`](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-setTapListener-com-here-sdk-gestures-TapListener" class="section detail">

    ### setTapListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTapListener</span><wbr></wbr><span class="parameters">(@Nullable [TapListener](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a TapListener that notifies when a tap gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`TapListener`](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures") that notifies when a tap gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-getDoubleTapListener" class="section detail">

    ### getDoubleTapListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[DoubleTapListener](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getDoubleTapListener</span>()

    </div>

    <div class="block">

    Gets a DoubleTapListener that notifies when a double-tap gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`DoubleTapListener`](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-setDoubleTapListener-com-here-sdk-gestures-DoubleTapListener" class="section detail">

    ### setDoubleTapListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDoubleTapListener</span><wbr></wbr><span class="parameters">(@Nullable [DoubleTapListener](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a DoubleTapListener that notifies when a double-tap gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`DoubleTapListener`](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures") that notifies when a double-tap gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-getPinchRotateListener" class="section detail">

    ### getPinchRotateListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[PinchRotateListener](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getPinchRotateListener</span>()

    </div>

    <div class="block">

    Gets a PinchRotateListener that notifies when a pinch-rotate gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`PinchRotateListener`](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-setPinchRotateListener-com-here-sdk-gestures-PinchRotateListener" class="section detail">

    ### setPinchRotateListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPinchRotateListener</span><wbr></wbr><span class="parameters">(@Nullable [PinchRotateListener](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a PinchRotateListener that notifies when a pinch-rotate gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`PinchRotateListener`](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures") that notifies when a pinch-rotate gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-getLongPressListener" class="section detail">

    ### getLongPressListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[LongPressListener](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getLongPressListener</span>()

    </div>

    <div class="block">

    Gets a LongPressListener that notifies when a long-press gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`LongPressListener`](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-setLongPressListener-com-here-sdk-gestures-LongPressListener" class="section detail">

    ### setLongPressListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLongPressListener</span><wbr></wbr><span class="parameters">(@Nullable [LongPressListener](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a LongPressListener that notifies when a long-press gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`LongPressListener`](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures") that notifies when a long-press gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-getPanListener" class="section detail">

    ### getPanListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[PanListener](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getPanListener</span>()

    </div>

    <div class="block">

    Gets a PanListener that notifies when a pan gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`PanListener`](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-setPanListener-com-here-sdk-gestures-PanListener" class="section detail">

    ### setPanListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPanListener</span><wbr></wbr><span class="parameters">(@Nullable [PanListener](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a PanListener that notifies when a pan gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`PanListener`](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures") that notifies when a pan gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-getTwoFingerTapListener" class="section detail">

    ### getTwoFingerTapListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[TwoFingerTapListener](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getTwoFingerTapListener</span>()

    </div>

    <div class="block">

    Gets a TwoFingerTapListener that notifies when a two-finger tap gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`TwoFingerTapListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-setTwoFingerTapListener-com-here-sdk-gestures-TwoFingerTapListener" class="section detail">

    ### setTwoFingerTapListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTwoFingerTapListener</span><wbr></wbr><span class="parameters">(@Nullable [TwoFingerTapListener](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a TwoFingerTapListener that notifies when a two-finger tap gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`TwoFingerTapListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures") that notifies when a two-finger tap gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-getTwoFingerPanListener" class="section detail">

    ### getTwoFingerPanListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[TwoFingerPanListener](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getTwoFingerPanListener</span>()

    </div>

    <div class="block">

    Gets a TwoFingerPanListener that notifies when a two-finger pan gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`TwoFingerPanListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-setTwoFingerPanListener-com-here-sdk-gestures-TwoFingerPanListener" class="section detail">

    ### setTwoFingerPanListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTwoFingerPanListener</span><wbr></wbr><span class="parameters">(@Nullable [TwoFingerPanListener](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a TwoFingerPanListener that notifies when a two-finger pan gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`TwoFingerPanListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures") that notifies when a two-finger pan gesture occurs.

    </div>

  - <div id="sdk-for-android-explore-getScrollHandler" class="section detail">

    ### getScrollHandler

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[ScrollHandler](sdk-for-android-explore-com-here-sdk-gestures-scrollhandler "class in com.here.sdk.gestures")</span> <span class="element-name">getScrollHandler</span>()

    </div>

    <div class="block">

    Returns scroll handler. See ScrollHandler.onScroll(float, float) for more details.

    </div>

    Returns:  
    Scroll handler.

    </div>

  - <div id="sdk-for-android-explore-getScaleHandler" class="section detail">

    ### getScaleHandler

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[ScaleHandler](sdk-for-android-explore-com-here-sdk-gestures-scalehandler "class in com.here.sdk.gestures")</span> <span class="element-name">getScaleHandler</span>()

    </div>

    <div class="block">

    Returns scale handler. See ScaleHandler.onScale(float, float, float) for more details.

    </div>

    Returns:  
    Scale handler.

    </div>

  - <div id="sdk-for-android-explore-getFlingHandler" class="section detail">

    ### getFlingHandler

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[FlingHandler](sdk-for-android-explore-com-here-sdk-gestures-flinghandler "class in com.here.sdk.gestures")</span> <span class="element-name">getFlingHandler</span>()

    </div>

    <div class="block">

    Returns fling handler. See FlingHandler.onFling(float, float) for more details.

    </div>

    Returns:  
    Fling handler.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

