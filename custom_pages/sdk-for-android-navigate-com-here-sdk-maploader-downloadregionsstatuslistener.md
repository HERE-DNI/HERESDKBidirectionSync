---
title: "DownloadRegionsStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DownloadRegionsStatusListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">DownloadRegionsStatusListener</span></div>
<div className="block"><p>Interface to get notified on
 status updates when downloading map regions.</p></div>
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
<section className="detail" id="onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)">
<h3>onDownloadRegionsComplete</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onDownloadRegionsComplete</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a>&gt; regions)</span></div>
<div className="block"><p>Called after the download for all requested regions has been completed with success or
 failure. In this callback, failure represents non-retryable error (eg. authentication failure
 because of invalid credentials and similars). Temporary failures (eg. network errors) are
 notified through <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener#onPause(com.here.sdk.maploader.MapLoaderError)"><code>onPause(com.here.sdk.maploader.MapLoaderError)</code></a> and downloads will be
 in paused state so they can be resumed later.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure. It is <code>null</code> for an operation that
     succeeds.</p></dd>
<dd><code>regions</code> - <p>Represents a list of regions which has been downloaded. It is <code>null</code> in case
     of an error.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onProgress(com.here.sdk.maploader.RegionId,int)">
<h3>onProgress</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onProgress</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> region,
 int percentage)</span></div>
<div className="block"><p>Called multiple times to indicate the download progress for each requested region
 individually.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>region</code> - <p>Represents an id of region status update is related to.</p></dd>
<dd><code>percentage</code> - <p>Represents a percentage of data which has been downloaded for particular
     region.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onPause(com.here.sdk.maploader.MapLoaderError)">
<h3>onPause</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onPause</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span></div>
<div className="block"><p>Called when download is paused.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Populated when retryable error is a reason of a pause. It is 'null' when pause
     is called by the user.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onResume()">
<h3>onResume</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onResume</span>()</div>
<div className="block"><p>Called when paused download is resumed.</p></div>
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
