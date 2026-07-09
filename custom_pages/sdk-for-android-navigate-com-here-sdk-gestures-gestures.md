---
title: "Gestures (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-gestures-gestures"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Gestures.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.gestures</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.gestures.Gestures</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Gestures</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Use this class to process touch events from the platform and detect gesture induced actions on the map view.
 Please note that this class holds strong references to the gesture listeners.
 On Android Auto, processing touch events is not needed. Instead, gestures get detected by android auto
 platform and provided via callbacks. For more information see onClick, onFling and onScale methods in
 <a href="https://developer.android.com/reference/androidx/car/app/SurfaceCallback">https://developer.android.com/reference/androidx/car/app/SurfaceCallback</a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="enableDefaultAction(com.here.sdk.gestures.GestureType)">
<h3>enableDefaultAction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">enableDefaultAction</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-gesturetype" title="enum class in com.here.sdk.gestures">GestureType</a> gestureType)</span></div>
<div className="block"><p>Enables default action to be performed for a specified
 gesture.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>gestureType</code> - <p>The gesture type.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="disableDefaultAction(com.here.sdk.gestures.GestureType)">
<h3>disableDefaultAction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">disableDefaultAction</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-gesturetype" title="enum class in com.here.sdk.gestures">GestureType</a> gestureType)</span></div>
<div className="block"><p>Disables default action for a specified gesture.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>gestureType</code> - <p>The gesture type.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTapListener()">
<h3>getTapListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-taplistener" title="interface in com.here.sdk.gestures">TapListener</a></span> <span className="element-name">getTapListener</span>()</div>
<div className="block"><p>Gets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs. <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-com-here-sdk-gestures-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTapListener(com.here.sdk.gestures.TapListener)">
<h3>setTapListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTapListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-taplistener" title="interface in com.here.sdk.gestures">TapListener</a> value)</span></div>
<div className="block"><p>Sets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-gestures-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDoubleTapListener()">
<h3>getDoubleTapListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-doubletaplistener" title="interface in com.here.sdk.gestures">DoubleTapListener</a></span> <span className="element-name">getDoubleTapListener</span>()</div>
<div className="block"><p>Gets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs. <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-com-here-sdk-gestures-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDoubleTapListener(com.here.sdk.gestures.DoubleTapListener)">
<h3>setDoubleTapListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDoubleTapListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-doubletaplistener" title="interface in com.here.sdk.gestures">DoubleTapListener</a> value)</span></div>
<div className="block"><p>Sets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-gestures-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPinchRotateListener()">
<h3>getPinchRotateListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener" title="interface in com.here.sdk.gestures">PinchRotateListener</a></span> <span className="element-name">getPinchRotateListener</span>()</div>
<div className="block"><p>Gets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs. <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPinchRotateListener(com.here.sdk.gestures.PinchRotateListener)">
<h3>setPinchRotateListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPinchRotateListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener" title="interface in com.here.sdk.gestures">PinchRotateListener</a> value)</span></div>
<div className="block"><p>Sets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLongPressListener()">
<h3>getLongPressListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-longpresslistener" title="interface in com.here.sdk.gestures">LongPressListener</a></span> <span className="element-name">getLongPressListener</span>()</div>
<div className="block"><p>Gets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs. <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-com-here-sdk-gestures-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setLongPressListener(com.here.sdk.gestures.LongPressListener)">
<h3>setLongPressListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setLongPressListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-longpresslistener" title="interface in com.here.sdk.gestures">LongPressListener</a> value)</span></div>
<div className="block"><p>Sets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-gestures-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPanListener()">
<h3>getPanListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-panlistener" title="interface in com.here.sdk.gestures">PanListener</a></span> <span className="element-name">getPanListener</span>()</div>
<div className="block"><p>Gets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs. <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-com-here-sdk-gestures-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPanListener(com.here.sdk.gestures.PanListener)">
<h3>setPanListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPanListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-panlistener" title="interface in com.here.sdk.gestures">PanListener</a> value)</span></div>
<div className="block"><p>Sets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-gestures-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTwoFingerTapListener()">
<h3>getTwoFingerTapListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingertaplistener" title="interface in com.here.sdk.gestures">TwoFingerTapListener</a></span> <span className="element-name">getTwoFingerTapListener</span>()</div>
<div className="block"><p>Gets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs. <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTwoFingerTapListener(com.here.sdk.gestures.TwoFingerTapListener)">
<h3>setTwoFingerTapListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTwoFingerTapListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingertaplistener" title="interface in com.here.sdk.gestures">TwoFingerTapListener</a> value)</span></div>
<div className="block"><p>Sets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTwoFingerPanListener()">
<h3>getTwoFingerPanListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingerpanlistener" title="interface in com.here.sdk.gestures">TwoFingerPanListener</a></span> <span className="element-name">getTwoFingerPanListener</span>()</div>
<div className="block"><p>Gets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs. <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTwoFingerPanListener(com.here.sdk.gestures.TwoFingerPanListener)">
<h3>setTwoFingerPanListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTwoFingerPanListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingerpanlistener" title="interface in com.here.sdk.gestures">TwoFingerPanListener</a> value)</span></div>
<div className="block"><p>Sets a <a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-gestures-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getScrollHandler()">
<h3>getScrollHandler</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-scrollhandler" title="class in com.here.sdk.gestures">ScrollHandler</a></span> <span className="element-name">getScrollHandler</span>()</div>
<div className="block"><p>Returns scroll handler. See <a href="sdk-for-android-navigate-scrollhandler#onScroll(float,float)"><code>ScrollHandler.onScroll(float, float)</code></a> for more details.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Scroll handler.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getScaleHandler()">
<h3>getScaleHandler</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-scalehandler" title="class in com.here.sdk.gestures">ScaleHandler</a></span> <span className="element-name">getScaleHandler</span>()</div>
<div className="block"><p>Returns scale handler. See <a href="sdk-for-android-navigate-scalehandler#onScale(float,float,float)"><code>ScaleHandler.onScale(float, float, float)</code></a> for more details.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Scale handler.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFlingHandler()">
<h3>getFlingHandler</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-flinghandler" title="class in com.here.sdk.gestures">FlingHandler</a></span> <span className="element-name">getFlingHandler</span>()</div>
<div className="block"><p>Returns fling handler. See <a href="sdk-for-android-navigate-flinghandler#onFling(float,float)"><code>FlingHandler.onFling(float, float)</code></a> for more details.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Fling handler.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
