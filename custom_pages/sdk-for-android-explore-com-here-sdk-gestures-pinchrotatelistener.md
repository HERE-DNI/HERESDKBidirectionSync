---
title: "PinchRotateListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PinchRotateListener.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.gestures</a></div>

</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">PinchRotateListener</span></div>
<div class="block"><p>Interface for handling pinch rotate gestures.
 Pinch rotate gesture occurs when two fingers are on the screen
 and at least one of them moves.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener#onPinchRotate(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double,com.here.sdk.core.Angle)">onPinchRotate</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-gestures-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state,
 <a href="sdk-for-android-explore-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> pinchOrigin,
 <a href="sdk-for-android-explore-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> rotationOrigin,
 double twoFingerDistance,
 <a href="sdk-for-android-explore-com-here-sdk-core-angle" title="class in com.here.sdk.core">Angle</a> rotation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when the pinch rotate gesture occurs.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="onPinchRotate(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double,com.here.sdk.core.Angle)">
<h3>onPinchRotate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onPinchRotate</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-gestures-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> pinchOrigin,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> rotationOrigin,
 double twoFingerDistance,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-core-angle" title="class in com.here.sdk.core">Angle</a> rotation)</span></div>
<div class="block"><p>Called when the pinch rotate gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - <p>Determines in which state the gesture is.</p></dd>
<dd><code>pinchOrigin</code> - <p>Position where the pinch happened relative to the MapView in pixels.</p></dd>
<dd><code>rotationOrigin</code> - <p>Position where the rotation happened relative to the MapView in pixels.</p></dd>
<dd><code>twoFingerDistance</code> - <p>Distance between the two fingers in pixels.</p></dd>
<dd><code>rotation</code> - <p>Fingers rotation angle delta. Indicates how much the fingers rotation angle has changed
     since the previous gesture update. Clockwise finger rotation gives positive deltas,
     counter clockwise finger rotation gives negative deltas.</p></dd>
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
