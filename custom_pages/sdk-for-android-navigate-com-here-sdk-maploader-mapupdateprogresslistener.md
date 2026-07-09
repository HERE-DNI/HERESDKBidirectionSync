---
title: "MapUpdateProgressListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdateprogresslistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapUpdateProgressListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">MapUpdateProgressListener</span></div>
<div className="block"><p>Interface to get notified on status updates
 when updating map data, previously downloaded by <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a>.</p></div>
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
<section className="detail" id="onProgress(com.here.sdk.maploader.RegionId,int)">
<h3>onProgress</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onProgress</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> region,
 int percentage)</span></div>
<div className="block"><p>Called multiple times to indicate the update progress.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>region</code> - <p>Represents an id of region status update is related to.</p></dd>
<dd><code>percentage</code> - <p>Represents a percentage of map data which has been updated.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onPause(com.here.sdk.maploader.MapLoaderError)">
<h3>onPause</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onPause</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span></div>
<div className="block"><p>Called when update is paused.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Populated when a retryable error is the reason for a pause. A retryable error can happen,
     when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection.
     In general, the HERE SDK will try a few times, before the update is paused.
     This error value gives a hint on the reason for the necessary retry operation.
     A paused download can be resumed by the user at a later time.
     It is 'null' when <code>MapUpdateTask.pause(boolean)</code> was called by the user.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onComplete(com.here.sdk.maploader.MapLoaderError)">
<h3>onComplete</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onComplete</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span></div>
<div className="block"><p>Called after the update process for all regions has been completed.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure.
     If an error occurs, the operation cannot be resumed later.
     It is <code>null</code> for an operation that succeeds.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onResume()">
<h3>onResume</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onResume</span>()</div>
<div className="block"><p>Called when a paused map update is resumed.</p></div>
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
