---
title: "Gestures (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-gestures"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.gestures](sdk-for-android-explore-com-here-sdk-gestures-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.gestures.Gestures →
com.here.NativeBase → com.here.sdk.gestures.Gestures

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Gestures</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Use this class to process touch events from the platform and detect
gesture induced actions on the map view. Please note that this class
holds strong references to the gesture listeners. On Android Auto,
processing touch events is not needed. Instead, gestures get detected by
android auto platform and provided via callbacks. For more information
see onClick, onFling and onScale methods in
https://developer.android.com/reference/androidx/car/app/SurfaceCallback
.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>disableDefaultAction(GestureType gestureType)</code></pre></td>
  <td><div class="block">
  Disables default action for a specified gesture.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>enableDefaultAction(GestureType gestureType)</code></pre></td>
  <td><div class="block">
  Enables default action to be performed for a specified gesture.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener"
  title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a></td>
  <td><pre><code>getDoubleTapListener()</code></pre></td>
  <td><div class="block">
  Gets a DoubleTapListener that notifies when a double-tap gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-gestures-flinghandler"
  title="class in com.here.sdk.gestures"><code>FlingHandler</code></a></td>
  <td><pre><code>getFlingHandler()</code></pre></td>
  <td><div class="block">
  Returns fling handler.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-gestures-longpresslistener"
  title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a></td>
  <td><pre><code>getLongPressListener()</code></pre></td>
  <td><div class="block">
  Gets a LongPressListener that notifies when a long-press gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-gestures-panlistener"
  title="interface in com.here.sdk.gestures"><code>PanListener</code></a></td>
  <td><pre><code>getPanListener()</code></pre></td>
  <td><div class="block">
  Gets a PanListener that notifies when a pan gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener"
  title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a></td>
  <td><pre><code>getPinchRotateListener()</code></pre></td>
  <td><div class="block">
  Gets a PinchRotateListener that notifies when a pinch-rotate gesture
  occurs.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-gestures-scalehandler"
  title="class in com.here.sdk.gestures"><code>ScaleHandler</code></a></td>
  <td><pre><code>getScaleHandler()</code></pre></td>
  <td><div class="block">
  Returns scale handler.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-gestures-scrollhandler"
  title="class in com.here.sdk.gestures"><code>ScrollHandler</code></a></td>
  <td><pre><code>getScrollHandler()</code></pre></td>
  <td><div class="block">
  Returns scroll handler.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-gestures-taplistener"
  title="interface in com.here.sdk.gestures"><code>TapListener</code></a></td>
  <td><pre><code>getTapListener()</code></pre></td>
  <td><div class="block">
  Gets a TapListener that notifies when a tap gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener"
  title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a></td>
  <td><pre><code>getTwoFingerPanListener()</code></pre></td>
  <td><div class="block">
  Gets a TwoFingerPanListener that notifies when a two-finger pan gesture
  occurs.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener"
  title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a></td>
  <td><pre><code>getTwoFingerTapListener()</code></pre></td>
  <td><div class="block">
  Gets a TwoFingerTapListener that notifies when a two-finger tap gesture
  occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setDoubleTapListener(DoubleTapListener value)</code></pre></td>
  <td><div class="block">
  Sets a DoubleTapListener that notifies when a double-tap gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setLongPressListener(LongPressListener value)</code></pre></td>
  <td><div class="block">
  Sets a LongPressListener that notifies when a long-press gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setPanListener(PanListener value)</code></pre></td>
  <td><div class="block">
  Sets a PanListener that notifies when a pan gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setPinchRotateListener(PinchRotateListener value)</code></pre></td>
  <td><div class="block">
  Sets a PinchRotateListener that notifies when a pinch-rotate gesture
  occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setTapListener(TapListener value)</code></pre></td>
  <td><div class="block">
  Sets a TapListener that notifies when a tap gesture occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setTwoFingerPanListener(TwoFingerPanListener value)</code></pre></td>
  <td><div class="block">
  Sets a TwoFingerPanListener that notifies when a two-finger pan gesture
  occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setTwoFingerTapListener(TwoFingerTapListener value)</code></pre></td>
  <td><div class="block">
  Sets a TwoFingerTapListener that notifies when a two-finger tap gesture
  occurs.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="enableDefaultAction(com.here.sdk.gestures.GestureType)"
    class="section detail">

    ### enableDefaultAction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableDefaultAction</span><span class="parameters">(@NonNull
    [GestureType](sdk-for-android-explore-com-here-sdk-gestures-gesturetype "enum class in com.here.sdk.gestures") gestureType)</span>

    </div>

    <div class="block">

    Enables default action to be performed for a specified gesture.

    </div>

    Parameters:  
    `gestureType` -

    The gesture type.

    </div>

  - <div id="disableDefaultAction(com.here.sdk.gestures.GestureType)"
    class="section detail">

    ### disableDefaultAction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disableDefaultAction</span><span class="parameters">(@NonNull
    [GestureType](sdk-for-android-explore-com-here-sdk-gestures-gesturetype "enum class in com.here.sdk.gestures") gestureType)</span>

    </div>

    <div class="block">

    Disables default action for a specified gesture.

    </div>

    Parameters:  
    `gestureType` -

    The gesture type.

    </div>

  - <div id="getTapListener()" class="section detail">

    ### getTapListener

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TapListener](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getTapListener</span>()

    </div>

    <div class="block">

    Gets a TapListener that notifies when a tap gesture occurs. Gestures
    holds a strong reference to the listener.

    </div>

    Returns:  
    [`TapListener`](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures")
    that notifies when a tap gesture occurs.

    </div>

  - <div id="setTapListener(com.here.sdk.gestures.TapListener)"
    class="section detail">

    ### setTapListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTapListener</span><span class="parameters">(@Nullable
    [TapListener](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a TapListener that notifies when a tap gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`TapListener`](sdk-for-android-explore-com-here-sdk-gestures-taplistener "interface in com.here.sdk.gestures")
    that notifies when a tap gesture occurs.

    </div>

  - <div id="getDoubleTapListener()" class="section detail">

    ### getDoubleTapListener

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[DoubleTapListener](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getDoubleTapListener</span>()

    </div>

    <div class="block">

    Gets a DoubleTapListener that notifies when a double-tap gesture
    occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`DoubleTapListener`](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures")
    that notifies when a double-tap gesture occurs.

    </div>

  - <div id="setDoubleTapListener(com.here.sdk.gestures.DoubleTapListener)"
    class="section detail">

    ### setDoubleTapListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDoubleTapListener</span><span class="parameters">(@Nullable
    [DoubleTapListener](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a DoubleTapListener that notifies when a double-tap gesture
    occurs.

    </div>

    Parameters:  
    `value` -

    [`DoubleTapListener`](sdk-for-android-explore-com-here-sdk-gestures-doubletaplistener "interface in com.here.sdk.gestures")
    that notifies when a double-tap gesture occurs.

    </div>

  - <div id="getPinchRotateListener()" class="section detail">

    ### getPinchRotateListener

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[PinchRotateListener](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getPinchRotateListener</span>()

    </div>

    <div class="block">

    Gets a PinchRotateListener that notifies when a pinch-rotate gesture
    occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`PinchRotateListener`](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures")
    that notifies when a pinch-rotate gesture occurs.

    </div>

  - <div id="setPinchRotateListener(com.here.sdk.gestures.PinchRotateListener)"
    class="section detail">

    ### setPinchRotateListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPinchRotateListener</span><span class="parameters">(@Nullable
    [PinchRotateListener](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a PinchRotateListener that notifies when a pinch-rotate gesture
    occurs.

    </div>

    Parameters:  
    `value` -

    [`PinchRotateListener`](sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener "interface in com.here.sdk.gestures")
    that notifies when a pinch-rotate gesture occurs.

    </div>

  - <div id="getLongPressListener()" class="section detail">

    ### getLongPressListener

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[LongPressListener](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getLongPressListener</span>()

    </div>

    <div class="block">

    Gets a LongPressListener that notifies when a long-press gesture
    occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`LongPressListener`](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures")
    that notifies when a long-press gesture occurs.

    </div>

  - <div id="setLongPressListener(com.here.sdk.gestures.LongPressListener)"
    class="section detail">

    ### setLongPressListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLongPressListener</span><span class="parameters">(@Nullable
    [LongPressListener](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a LongPressListener that notifies when a long-press gesture
    occurs.

    </div>

    Parameters:  
    `value` -

    [`LongPressListener`](sdk-for-android-explore-com-here-sdk-gestures-longpresslistener "interface in com.here.sdk.gestures")
    that notifies when a long-press gesture occurs.

    </div>

  - <div id="getPanListener()" class="section detail">

    ### getPanListener

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[PanListener](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getPanListener</span>()

    </div>

    <div class="block">

    Gets a PanListener that notifies when a pan gesture occurs. Gestures
    holds a strong reference to the listener.

    </div>

    Returns:  
    [`PanListener`](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures")
    that notifies when a pan gesture occurs.

    </div>

  - <div id="setPanListener(com.here.sdk.gestures.PanListener)"
    class="section detail">

    ### setPanListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPanListener</span><span class="parameters">(@Nullable
    [PanListener](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a PanListener that notifies when a pan gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`PanListener`](sdk-for-android-explore-com-here-sdk-gestures-panlistener "interface in com.here.sdk.gestures")
    that notifies when a pan gesture occurs.

    </div>

  - <div id="getTwoFingerTapListener()" class="section detail">

    ### getTwoFingerTapListener

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TwoFingerTapListener](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getTwoFingerTapListener</span>()

    </div>

    <div class="block">

    Gets a TwoFingerTapListener that notifies when a two-finger tap
    gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`TwoFingerTapListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures")
    that notifies when a two-finger tap gesture occurs.

    </div>

  - <div id="setTwoFingerTapListener(com.here.sdk.gestures.TwoFingerTapListener)"
    class="section detail">

    ### setTwoFingerTapListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTwoFingerTapListener</span><span class="parameters">(@Nullable
    [TwoFingerTapListener](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a TwoFingerTapListener that notifies when a two-finger tap
    gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`TwoFingerTapListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener "interface in com.here.sdk.gestures")
    that notifies when a two-finger tap gesture occurs.

    </div>

  - <div id="getTwoFingerPanListener()" class="section detail">

    ### getTwoFingerPanListener

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TwoFingerPanListener](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures")</span> <span class="element-name">getTwoFingerPanListener</span>()

    </div>

    <div class="block">

    Gets a TwoFingerPanListener that notifies when a two-finger pan
    gesture occurs. Gestures holds a strong reference to the listener.

    </div>

    Returns:  
    [`TwoFingerPanListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures")
    that notifies when a two-finger pan gesture occurs.

    </div>

  - <div id="setTwoFingerPanListener(com.here.sdk.gestures.TwoFingerPanListener)"
    class="section detail">

    ### setTwoFingerPanListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTwoFingerPanListener</span><span class="parameters">(@Nullable
    [TwoFingerPanListener](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures") value)</span>

    </div>

    <div class="block">

    Sets a TwoFingerPanListener that notifies when a two-finger pan
    gesture occurs.

    </div>

    Parameters:  
    `value` -

    [`TwoFingerPanListener`](sdk-for-android-explore-com-here-sdk-gestures-twofingerpanlistener "interface in com.here.sdk.gestures")
    that notifies when a two-finger pan gesture occurs.

    </div>

  - <div id="getScrollHandler()" class="section detail">

    ### getScrollHandler

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[ScrollHandler](sdk-for-android-explore-com-here-sdk-gestures-scrollhandler "class in com.here.sdk.gestures")</span> <span class="element-name">getScrollHandler</span>()

    </div>

    <div class="block">

    Returns scroll handler. See ScrollHandler.onScroll(float, float) for
    more details.

    </div>

    Returns:  
    Scroll handler.

    </div>

  - <div id="getScaleHandler()" class="section detail">

    ### getScaleHandler

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[ScaleHandler](sdk-for-android-explore-com-here-sdk-gestures-scalehandler "class in com.here.sdk.gestures")</span> <span class="element-name">getScaleHandler</span>()

    </div>

    <div class="block">

    Returns scale handler. See ScaleHandler.onScale(float, float, float)
    for more details.

    </div>

    Returns:  
    Scale handler.

    </div>

  - <div id="getFlingHandler()" class="section detail">

    ### getFlingHandler

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[FlingHandler](sdk-for-android-explore-com-here-sdk-gestures-flinghandler "class in com.here.sdk.gestures")</span> <span class="element-name">getFlingHandler</span>()

    </div>

    <div class="block">

    Returns fling handler. See FlingHandler.onFling(float, float) for
    more details.

    </div>

    Returns:  
    Fling handler.

    </div>

  </div>

</div>

