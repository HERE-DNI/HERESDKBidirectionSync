---
title: "W3WSearchCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-w3wsearchcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- W3WSearchCallback.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-search-package-summary">com.here.sdk.search</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">W3WSearchCallback</span></div>
<div class="block"><p>The method that will be called on the main thread when a search operation in <code>W3WSearchEngine</code>
 has been completed.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onW3WSearchCompleted(com.here.sdk.search.W3WSearchError,com.here.sdk.search.W3WSquare)">onW3WSearchCompleted</a><wbr/>(<a href="sdk-for-android-navigate-w3wsearcherror" title="enum class in com.here.sdk.search">W3WSearchError</a> searchError,
 <a href="sdk-for-android-navigate-w3wsquare" title="class in com.here.sdk.search">W3WSquare</a> square)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The method that will be called on the main thread when a search operation in <code>W3WSearchEngine</code>
 has been completed.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="onW3WSearchCompleted(com.here.sdk.search.W3WSearchError,com.here.sdk.search.W3WSquare)">
<h3>onW3WSearchCompleted</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onW3WSearchCompleted</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-w3wsearcherror" title="enum class in com.here.sdk.search">W3WSearchError</a> searchError,
 @Nullable
 <a href="sdk-for-android-navigate-w3wsquare" title="class in com.here.sdk.search">W3WSquare</a> square)</span></div>
<div class="block"><p>The method that will be called on the main thread when a search operation in <code>W3WSearchEngine</code>
 has been completed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>searchError</code> - <p>The w3w search error.</p></dd>
<dd><code>square</code> - <p>The w3w square.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
