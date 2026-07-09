---
title: "MapDownloaderTask (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapDownloaderTask.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.maploader.MapDownloaderTask</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapDownloaderTask</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A class to control map download process.</p></div>
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
<section className="detail" id="cancel()">
<h3>cancel</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">cancel</span>()</div>
<div className="block"><p>Cancels the ongoing map download operation. Operation cannot be resumed afterwards.
 It will do nothing if the task was already cancelled or has been completed.
 Status of the call will be reported via <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a>.
 <a href="sdk-for-android-navigate-maploadererror#OPERATION_CANCELLED"><code>MapLoaderError.OPERATION_CANCELLED</code></a> will be reported for successful cancel.</p></div>
</section>
</li>
<li>
<section className="detail" id="pause()">
<h3>pause</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">pause</span>()</div>
<div className="block"><p>Pauses the ongoing map download operation. Operation can be resumed afterwards.
 It will do nothing if operation is not in running state.
 Status of the call will be reported via <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onPause(com.here.sdk.maploader.MapLoaderError)"><code>DownloadRegionsStatusListener.onPause(com.here.sdk.maploader.MapLoaderError)</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="resume()">
<h3>resume</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">resume</span>()</div>
<div className="block"><p>Resumes paused map download operation. It will do nothing if operation is not in
 paused state.
 Status of the call will be reported via <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onResume()"><code>DownloadRegionsStatusListener.onResume()</code></a>.</p></div>
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
