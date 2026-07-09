---
title: "PinchRotateListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PinchRotateListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.gestures</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">PinchRotateListener</span></div>
<div className="block"><p>Interface for handling pinch rotate gestures.
 Pinch rotate gesture occurs when two fingers are on the screen
 and at least one of them moves.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="onPinchRotate(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double,com.here.sdk.core.Angle)">
<h3>onPinchRotate</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onPinchRotate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> pinchOrigin,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> rotationOrigin,
 double twoFingerDistance,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-angle" title="class in com.here.sdk.core">Angle</a> rotation)</span></div>
<div className="block"><p>Called when the pinch rotate gesture occurs.</p></div>
<dl className="notes">
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
