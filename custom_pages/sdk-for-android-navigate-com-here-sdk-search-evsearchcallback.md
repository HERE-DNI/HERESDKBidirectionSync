---
title: "EVSearchCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evsearchcallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EVSearchCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">EVSearchCallback</span></div>
<div className="block"><p>The method that will be called on the main thread when a search operation in <code>EVSearchEngine</code>
 has been completed.
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
<section className="detail" id="onEVCP3SearchCompleted(com.here.sdk.search.EVSearchError,java.util.List)">
<h3>onEVCP3SearchCompleted</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onEVCP3SearchCompleted</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a> error,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a>&gt; chargingLocations)</span></div>
<div className="block"><p>The method that will be called on the main thread when a search operation in <code>EVSearchEngine</code>
 has been completed.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>The ev search error.</p></dd>
<dd><code>chargingLocations</code> - <p>The ev charging locations.</p></dd>
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
