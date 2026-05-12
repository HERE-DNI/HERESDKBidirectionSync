---
title: "Gestures (API Reference)"
slug: "sdk-for-android-explore-gestures"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Gestures.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.gestures</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.gestures.Gestures</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Gestures</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Use this class to process touch events from the platform and detect gesture induced actions on the map view.
 Please note that this class holds strong references to the gesture listeners.
 On Android Auto, processing touch events is not needed. Instead, gestures get detected by android auto
 platform and provided via callbacks. For more information see onClick, onFling and onScale methods in
 <a href="https://developer.android.com/reference/androidx/car/app/SurfaceCallback">https://developer.android.com/reference/androidx/car/app/SurfaceCallback</a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disableDefaultAction(com.here.sdk.gestures.GestureType)">disableDefaultAction</a><wbr/>(<a href="sdk-for-android-explore-gesturetype" title="enum class in com.here.sdk.gestures">GestureType</a> gestureType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disables default action for a specified gesture.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enableDefaultAction(com.here.sdk.gestures.GestureType)">enableDefaultAction</a><wbr/>(<a href="sdk-for-android-explore-gesturetype" title="enum class in com.here.sdk.gestures">GestureType</a> gestureType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables default action to be performed for a specified
 gesture.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures">DoubleTapListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDoubleTapListener()">getDoubleTapListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-flinghandler" title="class in com.here.sdk.gestures">FlingHandler</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFlingHandler()">getFlingHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns fling handler.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures">LongPressListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLongPressListener()">getLongPressListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures">PanListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPanListener()">getPanListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures">PinchRotateListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPinchRotateListener()">getPinchRotateListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-scalehandler" title="class in com.here.sdk.gestures">ScaleHandler</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaleHandler()">getScaleHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns scale handler.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-scrollhandler" title="class in com.here.sdk.gestures">ScrollHandler</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getScrollHandler()">getScrollHandler</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns scroll handler.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures">TapListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTapListener()">getTapListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures">TwoFingerPanListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTwoFingerPanListener()">getTwoFingerPanListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures">TwoFingerTapListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTwoFingerTapListener()">getTwoFingerTapListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDoubleTapListener(com.here.sdk.gestures.DoubleTapListener)">setDoubleTapListener</a><wbr/>(<a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures">DoubleTapListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLongPressListener(com.here.sdk.gestures.LongPressListener)">setLongPressListener</a><wbr/>(<a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures">LongPressListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPanListener(com.here.sdk.gestures.PanListener)">setPanListener</a><wbr/>(<a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures">PanListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPinchRotateListener(com.here.sdk.gestures.PinchRotateListener)">setPinchRotateListener</a><wbr/>(<a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures">PinchRotateListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTapListener(com.here.sdk.gestures.TapListener)">setTapListener</a><wbr/>(<a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures">TapListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTwoFingerPanListener(com.here.sdk.gestures.TwoFingerPanListener)">setTwoFingerPanListener</a><wbr/>(<a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures">TwoFingerPanListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTwoFingerTapListener(com.here.sdk.gestures.TwoFingerTapListener)">setTwoFingerTapListener</a><wbr/>(<a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures">TwoFingerTapListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="enableDefaultAction(com.here.sdk.gestures.GestureType)">
<h3>enableDefaultAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableDefaultAction</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-gesturetype" title="enum class in com.here.sdk.gestures">GestureType</a> gestureType)</span></div>
<div class="block"><p>Enables default action to be performed for a specified
 gesture.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>gestureType</code> - <p>The gesture type.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disableDefaultAction(com.here.sdk.gestures.GestureType)">
<h3>disableDefaultAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disableDefaultAction</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-gesturetype" title="enum class in com.here.sdk.gestures">GestureType</a> gestureType)</span></div>
<div class="block"><p>Disables default action for a specified gesture.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>gestureType</code> - <p>The gesture type.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTapListener()">
<h3>getTapListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures">TapListener</a></span> <span class="element-name">getTapListener</span>()</div>
<div class="block"><p>Gets a <a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs. <a href="sdk-for-android-explore-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTapListener(com.here.sdk.gestures.TapListener)">
<h3>setTapListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTapListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures">TapListener</a> value)</span></div>
<div class="block"><p>Sets a <a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-explore-taplistener" title="interface in com.here.sdk.gestures"><code>TapListener</code></a> that notifies when a tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDoubleTapListener()">
<h3>getDoubleTapListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures">DoubleTapListener</a></span> <span class="element-name">getDoubleTapListener</span>()</div>
<div class="block"><p>Gets a <a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs. <a href="sdk-for-android-explore-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDoubleTapListener(com.here.sdk.gestures.DoubleTapListener)">
<h3>setDoubleTapListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDoubleTapListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures">DoubleTapListener</a> value)</span></div>
<div class="block"><p>Sets a <a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-explore-doubletaplistener" title="interface in com.here.sdk.gestures"><code>DoubleTapListener</code></a> that notifies when a double-tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPinchRotateListener()">
<h3>getPinchRotateListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures">PinchRotateListener</a></span> <span class="element-name">getPinchRotateListener</span>()</div>
<div class="block"><p>Gets a <a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs. <a href="sdk-for-android-explore-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPinchRotateListener(com.here.sdk.gestures.PinchRotateListener)">
<h3>setPinchRotateListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPinchRotateListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures">PinchRotateListener</a> value)</span></div>
<div class="block"><p>Sets a <a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-explore-pinchrotatelistener" title="interface in com.here.sdk.gestures"><code>PinchRotateListener</code></a> that notifies when a pinch-rotate gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLongPressListener()">
<h3>getLongPressListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures">LongPressListener</a></span> <span class="element-name">getLongPressListener</span>()</div>
<div class="block"><p>Gets a <a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs. <a href="sdk-for-android-explore-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLongPressListener(com.here.sdk.gestures.LongPressListener)">
<h3>setLongPressListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLongPressListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures">LongPressListener</a> value)</span></div>
<div class="block"><p>Sets a <a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-explore-longpresslistener" title="interface in com.here.sdk.gestures"><code>LongPressListener</code></a> that notifies when a long-press gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPanListener()">
<h3>getPanListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures">PanListener</a></span> <span class="element-name">getPanListener</span>()</div>
<div class="block"><p>Gets a <a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs. <a href="sdk-for-android-explore-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPanListener(com.here.sdk.gestures.PanListener)">
<h3>setPanListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPanListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures">PanListener</a> value)</span></div>
<div class="block"><p>Sets a <a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-explore-panlistener" title="interface in com.here.sdk.gestures"><code>PanListener</code></a> that notifies when a pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTwoFingerTapListener()">
<h3>getTwoFingerTapListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures">TwoFingerTapListener</a></span> <span class="element-name">getTwoFingerTapListener</span>()</div>
<div class="block"><p>Gets a <a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs. <a href="sdk-for-android-explore-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTwoFingerTapListener(com.here.sdk.gestures.TwoFingerTapListener)">
<h3>setTwoFingerTapListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTwoFingerTapListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures">TwoFingerTapListener</a> value)</span></div>
<div class="block"><p>Sets a <a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-explore-twofingertaplistener" title="interface in com.here.sdk.gestures"><code>TwoFingerTapListener</code></a> that notifies when a two-finger tap gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTwoFingerPanListener()">
<h3>getTwoFingerPanListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures">TwoFingerPanListener</a></span> <span class="element-name">getTwoFingerPanListener</span>()</div>
<div class="block"><p>Gets a <a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs. <a href="sdk-for-android-explore-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> holds a strong reference to the listener.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTwoFingerPanListener(com.here.sdk.gestures.TwoFingerPanListener)">
<h3>setTwoFingerPanListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTwoFingerPanListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures">TwoFingerPanListener</a> value)</span></div>
<div class="block"><p>Sets a <a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><a href="sdk-for-android-explore-twofingerpanlistener" title="interface in com.here.sdk.gestures"><code>TwoFingerPanListener</code></a> that notifies when a two-finger pan gesture occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScrollHandler()">
<h3>getScrollHandler</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-scrollhandler" title="class in com.here.sdk.gestures">ScrollHandler</a></span> <span class="element-name">getScrollHandler</span>()</div>
<div class="block"><p>Returns scroll handler. See <a href="sdk-for-android-explore-scrollhandler#onScroll(float,float)"><code>ScrollHandler.onScroll(float, float)</code></a> for more details.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Scroll handler.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScaleHandler()">
<h3>getScaleHandler</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-scalehandler" title="class in com.here.sdk.gestures">ScaleHandler</a></span> <span class="element-name">getScaleHandler</span>()</div>
<div class="block"><p>Returns scale handler. See <a href="sdk-for-android-explore-scalehandler#onScale(float,float,float)"><code>ScaleHandler.onScale(float, float, float)</code></a> for more details.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Scale handler.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFlingHandler()">
<h3>getFlingHandler</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-flinghandler" title="class in com.here.sdk.gestures">FlingHandler</a></span> <span class="element-name">getFlingHandler</span>()</div>
<div class="block"><p>Returns fling handler. See <a href="sdk-for-android-explore-flinghandler#onFling(float,float)"><code>FlingHandler.onFling(float, float)</code></a> for more details.</p></div>
<dl class="notes">
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
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
