---
title: "DownloadableRegionsCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-downloadableregionscallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DownloadableRegionsCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">DownloadableRegionsCallback</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)"><code>MapDownloader.getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)</code></a> has been completed.
 The first argument indicates an error in case of a failure. The second argument contains the results.
 Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p></div>
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
<section className="detail" id="onCompleted(com.here.sdk.maploader.MapLoaderError,java.util.List)">
<h3>onCompleted</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onCompleted</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> maploaderError,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader">Region</a>&gt; regions)</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)"><code>MapDownloader.getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)</code></a> has been completed.
 The first argument indicates an error in case of a failure. The second argument contains the results.
 Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>maploaderError</code> - <p>Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p></dd>
<dd><code>regions</code> - <p>Represents a list of downloadable regions. It is <code>null</code> in case of an error. Each region can contain child
     regions that can contain child regions and so on. Usually, the top-level regions represent continents that contain countries
     as children.</p></dd>
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
