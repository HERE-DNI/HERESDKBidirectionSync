---
title: "PrefetchStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PrefetchStatusListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.prefetcher</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">PrefetchStatusListener</span></div>
<div className="block"><p>Interface to get notified on status updates
 when prefetching map data.</p></div>
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
<section className="detail" id="onProgress(int)">
<h3>onProgress</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onProgress</span><wbr/><span className="parameters">(int percentage)</span></div>
<div className="block"><p>Called multiple times to indicate the update progress.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>percentage</code> - <p>Represents a percentage of corridor data which has been downloaded.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onComplete(com.here.sdk.maploader.MapLoaderError)">
<h3>onComplete</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onComplete</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span></div>
<div className="block"><p>Called after the geo-corridor data downloads has been completed either with success or with error.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure.
     If an error occurs, to resume operation, please download geo-corridor again.
     It is <code>null</code> for an operation that succeeds.</p></dd>
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
