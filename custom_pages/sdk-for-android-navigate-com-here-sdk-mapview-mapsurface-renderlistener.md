---
title: "MapSurface.RenderListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapsurface-renderlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapSurface.RenderListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface" title="class in com.here.sdk.mapview">MapSurface</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static interface </span><span className="element-name type-name-label">MapSurface.RenderListener</span></div>
<div className="block">Listener of MapSurface render events.

 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</div>
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
<section className="detail" id="onFramePrepared()">
<h3>onFramePrepared</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onFramePrepared</span>()</div>
<div className="block">Called after each frame is prepared for rendering, before presenting it, from inside the
 render loop. Inside, custom rendering can be performed. It is recommended that the
 execution to be kept to a minimum as this can adversely affect the frame rendering time.</div>
</section>
</li>
<li>
<section className="detail" id="onRenderTargetReleased()">
<h3>onRenderTargetReleased</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onRenderTargetReleased</span>()</div>
<div className="block">Called after the render target has been released.
 Inside, resources associated with any custom rendering can be released.</div>
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
