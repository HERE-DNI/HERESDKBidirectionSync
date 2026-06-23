---
title: "EVSearchError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evsearcherror"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EVSearchError.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a>&gt;
<div class="inheritance">com.here.sdk.search.EVSearchError</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">EVSearchError</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a>&gt;</span></div>
<div class="block"><p>Specifies possible errors that <code>EVSearchEngine</code> may report.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#AUTHENTICATION_FAILED">AUTHENTICATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">EVCP3 operation is not authenticated.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#BAD_REQUEST">BAD_REQUEST</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Something wrong or missing in the request.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#EMPTY_IDS">EMPTY_IDS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Empty list of IDs passed.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#EXCEEDED_USAGE_LIMIT">EXCEEDED_USAGE_LIMIT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Credentials exceeded the allowed requests limit.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#HTTP_ERROR">HTTP_ERROR</a></code></div>
<div class="col-last even-row-color">
<div class="block">A general network request error.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#INTERNAL_ERROR">INTERNAL_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Generic internal error.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#INVALID_ID">INVALID_ID</a></code></div>
<div class="col-last even-row-color">
<div class="block">At least one empty or invalid ID passed.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#NO_RESULTS_FOUND">NO_RESULTS_FOUND</a></code></div>
<div class="col-last odd-row-color">
<div class="block">No results found.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OFFLINE">OFFLINE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The device has no internet connection.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OPERATION_CANCELLED">OPERATION_CANCELLED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The request was cancelled (usually by the user).</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OPERATION_FAILED">OPERATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Search operation failed due to some reason.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PARSING_ERROR">PARSING_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">EVCP3 backend returns result with unexpected json schema.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PROXY_AUTHENTICATION_FAILED">PROXY_AUTHENTICATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Proxy is not authenticated.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PROXY_SERVER_UNREACHABLE">PROXY_SERVER_UNREACHABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Proxy server unreachable.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#SERVER_UNREACHABLE">SERVER_UNREACHABLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">EVCP3 server is unreachable.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#TIMED_OUT">TIMED_OUT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The request timed out.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="EMPTY_IDS">
<h3>EMPTY_IDS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">EMPTY_IDS</span></div>
<div class="block"><p>Empty list of IDs passed.</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_ID">
<h3>INVALID_ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">INVALID_ID</span></div>
<div class="block"><p>At least one empty or invalid ID passed.</p></div>
</section>
</li>
<li>
<section class="detail" id="BAD_REQUEST">
<h3>BAD_REQUEST</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">BAD_REQUEST</span></div>
<div class="block"><p>Something wrong or missing in the request.</p></div>
</section>
</li>
<li>
<section class="detail" id="PARSING_ERROR">
<h3>PARSING_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">PARSING_ERROR</span></div>
<div class="block"><p>EVCP3 backend returns result with unexpected json schema.</p></div>
</section>
</li>
<li>
<section class="detail" id="INTERNAL_ERROR">
<h3>INTERNAL_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">INTERNAL_ERROR</span></div>
<div class="block"><p>Generic internal error.</p></div>
</section>
</li>
<li>
<section class="detail" id="SERVER_UNREACHABLE">
<h3>SERVER_UNREACHABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">SERVER_UNREACHABLE</span></div>
<div class="block"><p>EVCP3 server is unreachable.</p></div>
</section>
</li>
<li>
<section class="detail" id="HTTP_ERROR">
<h3>HTTP_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">HTTP_ERROR</span></div>
<div class="block"><p>A general network request error.</p></div>
</section>
</li>
<li>
<section class="detail" id="AUTHENTICATION_FAILED">
<h3>AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">AUTHENTICATION_FAILED</span></div>
<div class="block"><p>EVCP3 operation is not authenticated. Check your credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="EXCEEDED_USAGE_LIMIT">
<h3>EXCEEDED_USAGE_LIMIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">EXCEEDED_USAGE_LIMIT</span></div>
<div class="block"><p>Credentials exceeded the allowed requests limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="TIMED_OUT">
<h3>TIMED_OUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">TIMED_OUT</span></div>
<div class="block"><p>The request timed out.</p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE">
<h3>OFFLINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">OFFLINE</span></div>
<div class="block"><p>The device has no internet connection.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_CANCELLED">
<h3>OPERATION_CANCELLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">OPERATION_CANCELLED</span></div>
<div class="block"><p>The request was cancelled (usually by the user).</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_AUTHENTICATION_FAILED">
<h3>PROXY_AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span></div>
<div class="block"><p>Proxy is not authenticated. Check your proxy credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_SERVER_UNREACHABLE">
<h3>PROXY_SERVER_UNREACHABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span></div>
<div class="block"><p>Proxy server unreachable.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_RESULTS_FOUND">
<h3>NO_RESULTS_FOUND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">NO_RESULTS_FOUND</span></div>
<div class="block"><p>No results found.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_FAILED">
<h3>OPERATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">OPERATION_FAILED</span></div>
<div class="block"><p>Search operation failed due to some reason.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-evsearcherror" title="enum class in com.here.sdk.search">EVSearchError</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
`
}</HTMLBlock>
