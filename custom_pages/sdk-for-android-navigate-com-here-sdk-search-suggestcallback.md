---
title: "SuggestCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-suggestcallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SuggestCallback.html -->






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
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">SuggestCallback</span></div>
<div className="block"><p>The method will be called on the main thread when a suggest call has been completed.
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
<section className="detail" id="onSuggestCompleted(com.here.sdk.search.SearchError,java.util.List)">
<h3>onSuggestCompleted</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onSuggestCompleted</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a> searchError,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search">Suggestion</a>&gt; suggestions)</span></div>
<div className="block"><p>The method will be called on the main thread when a suggest call has been completed.
 The first argument indicates an error in case of a failure. The second argument contains the results.
 Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>searchError</code> - <p>An error enum indicating what went wrong. It is <code>null</code> for an operation that succeeds.</p></dd>
<dd><code>suggestions</code> - <p>The list of suggestion results. It is <code>null</code> in case of an error.</p></dd>
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
