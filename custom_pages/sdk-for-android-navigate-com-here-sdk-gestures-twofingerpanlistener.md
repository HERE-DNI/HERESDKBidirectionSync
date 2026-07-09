---
title: "TwoFingerPanListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-gestures-twofingerpanlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TwoFingerPanListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.gestures</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TwoFingerPanListener</span></div>
<div className="block"><p>Interface for handling two finger pan gestures.
 Two finger pan gesture occurs when two fingers are on the screen
 and both of them are moving vertically.</p></div>
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
<section className="detail" id="onTwoFingerPan(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double)">
<h3>onTwoFingerPan</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onTwoFingerPan</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-gestures-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> translation,
 double velocity)</span></div>
<div className="block"><p>Called when the two finger pan gesture occurs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - <p>Determines in which state the gesture is.</p></dd>
<dd><code>origin</code> - <p>Position halfway between two touch points relative to the MapView in pixels.</p></dd>
<dd><code>translation</code> - <p>Translation offset since the last position in pixels.</p></dd>
<dd><code>velocity</code> - <p>Velocity of panning in pixels per millisecond.</p></dd>
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
