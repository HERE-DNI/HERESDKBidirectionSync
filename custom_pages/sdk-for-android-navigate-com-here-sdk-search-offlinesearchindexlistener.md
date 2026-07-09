---
title: "OfflineSearchIndexListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-offlinesearchindexlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- OfflineSearchIndexListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">OfflineSearchIndexListener</span></div>
<div className="block"><p>Interface to get updates about progress
 of creating persistent map index.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<section className="detail" id="onStarted(com.here.sdk.search.OfflineSearchIndex.Operation)">
<h3>onStarted</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onStarted</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindex-operation" title="enum class in com.here.sdk.search">OfflineSearchIndex.Operation</a> operation)</span></div>
<div className="block"><p>Called each time that the indexing has started. It is triggered by changes to persistent map
 or by calling <code>OfflineSearchEngine.setIndexOptions</code>.
 If a valid index was previously created for the installed regions, no additional indexing
 is performed, so no notifications are sent. In this context, a valid index is the one
 that contains data for the exact versions of the installed map regions. When any of them
 is updated or new regions are downloaded or deleted, the index becomes invalid and is
 automatically rebuilt, as long as indexing has been enabled previously.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - <p>Shows whether the index is being created or removed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onProgress(int)">
<h3>onProgress</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onProgress</span><wbr/><span className="parameters">(int percentage)</span></div>
<div className="block"><p>Called multiple times to indicate the progress of index creation or deletion.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>percentage</code> - <p>Represents a percentage of work done.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onComplete(com.here.sdk.search.OfflineSearchIndex.Error)">
<h3>onComplete</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onComplete</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindex-error" title="enum class in com.here.sdk.search">OfflineSearchIndex.Error</a> error)</span></div>
<div className="block"><p>Called after index creation or deletion has been completed.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure.
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
