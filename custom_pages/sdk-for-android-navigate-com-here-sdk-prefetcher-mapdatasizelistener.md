---
title: "MapDataSizeListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-mapdatasizelistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapDataSizeListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.prefetcher</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">MapDataSizeListener</span></div>
<div className="block"><p>Interface to get the result of map data size
 estimation.</p></div>
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
<section className="detail" id="onSizeEstimated(com.here.sdk.maploader.MapLoaderError,com.here.sdk.prefetcher.MapDataSize)">
<h3>onSizeEstimated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onSizeEstimated</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-mapdatasize" title="class in com.here.sdk.prefetcher">MapDataSize</a> dataSize)</span></div>
<div className="block"><p>Called after map data size estimation has been completed either with success or with error.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure. If the operation was successful,
     <code>null</code> is returned.</p></dd>
<dd><code>dataSize</code> - <p>Represents the map data size. In case of failure,
     <code>null</code> is returned.</p></dd>
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
