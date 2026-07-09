---
title: "EVSearchInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evsearchinterface"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EVSearchInterface.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-search-evsearchengine" title="class in com.here.sdk.search">EVSearchEngine</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">EVSearchInterface</span></div>
<div className="block"><p>Provides the interface for the <code>EVSearchEngine</code>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<section className="detail" id="search(java.util.List,com.here.sdk.search.EVSearchCallback)">
<h3>search</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">search</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-evsearchcallback" title="interface in com.here.sdk.search">EVSearchCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous request for <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocation" title="class in com.here.sdk.search"><code>EVChargingLocation</code></a> instances with given Place IDs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>ids</code> - <p>List of charging location identifiers.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
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
