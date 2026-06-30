---
title: "SearchError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-searcherror"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SearchError.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a>&gt;
<div class="inheritance">com.here.sdk.search.SearchError</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">SearchError</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a>&gt;</span></div>
<div class="block"><p>Specifies possible errors that may result from a search query.</p></div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#AUTHENTICATION_FAILED">AUTHENTICATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Search operation is not authenticated.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#BAD_REQUEST">BAD_REQUEST</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Bad network request</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#EXCEEDED_USAGE_LIMIT">EXCEEDED_USAGE_LIMIT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Credentials exceeded the allowed requests limit.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#FILTER_EMPTY">FILTER_EMPTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Filter is empty</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#FILTER_TOO_LONG">FILTER_TOO_LONG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Filter is too long, max.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#FORBIDDEN">FORBIDDEN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The credentials given do not provide access to the resource requested.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#HTTP_ERROR">HTTP_ERROR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Network request error.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#INVALID_AREA">INVALID_AREA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Box or circle area of query is invalid</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#INVALID_CORRIDOR_POLYLINE">INVALID_CORRIDOR_POLYLINE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Corridor area polyline size is less than 2 points</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#INVALID_CUSTOM_OPTION_FORMAT">INVALID_CUSTOM_OPTION_FORMAT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Custom options are set in an invalid format in the query</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#INVALID_TRUCK_CLASS">INVALID_TRUCK_CLASS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Light truck class is passed in the filter</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#INVALID_URL">INVALID_URL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Url is invalid</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#LAYERS_NOT_DOWNLOADED">LAYERS_NOT_DOWNLOADED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Downloaded regions missing <a href="sdk-for-android-navigate-layerconfiguration.feature#OFFLINE_SEARCH_GLOBAL"><code>LayerConfiguration.Feature.OFFLINE_SEARCH_GLOBAL</code></a>
 feature.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#MAP_NOT_READY">MAP_NOT_READY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Offline map data is incomplete for the requested operation.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#MAX_ITEMS_OUT_OF_RANGE">MAX_ITEMS_OUT_OF_RANGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Should be in the range [1, 100].</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#NO_RESULTS_FOUND">NO_RESULTS_FOUND</a></code></div>
<div class="col-last odd-row-color">
<div class="block">No results found.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#OFFLINE">OFFLINE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The device does not have an internet connection.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#OPERATION_CANCELLED">OPERATION_CANCELLED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Operation cancelled.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#OPERATION_FAILED">OPERATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operation failed due to an internal error.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#PARSING_ERROR">PARSING_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Error while parsing response data.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#PROXY_AUTHENTICATION_FAILED">PROXY_AUTHENTICATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Proxy is not authenticated.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#PROXY_SERVER_UNREACHABLE">PROXY_SERVER_UNREACHABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Proxy server unreachable.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#QUERY_EMPTY">QUERY_EMPTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Empty query</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#QUERY_TOO_LONG">QUERY_TOO_LONG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Query is too long, max.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#SERVER_UNREACHABLE">SERVER_UNREACHABLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Server unreachable.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#TIMED_OUT">TIMED_OUT</a></code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-searcherror#values()">values</a>()</code></div>
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
<section class="detail" id="AUTHENTICATION_FAILED">
<h3>AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">AUTHENTICATION_FAILED</span></div>
<div class="block"><p>Search operation is not authenticated. Check your credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="MAX_ITEMS_OUT_OF_RANGE">
<h3>MAX_ITEMS_OUT_OF_RANGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">MAX_ITEMS_OUT_OF_RANGE</span></div>
<div class="block"><p>Should be in the range [1, 100].</p></div>
</section>
</li>
<li>
<section class="detail" id="PARSING_ERROR">
<h3>PARSING_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">PARSING_ERROR</span></div>
<div class="block"><p>Error while parsing response data.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_RESULTS_FOUND">
<h3>NO_RESULTS_FOUND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">NO_RESULTS_FOUND</span></div>
<div class="block"><p>No results found.</p></div>
</section>
</li>
<li>
<section class="detail" id="HTTP_ERROR">
<h3>HTTP_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">HTTP_ERROR</span></div>
<div class="block"><p>Network request error.</p></div>
</section>
</li>
<li>
<section class="detail" id="SERVER_UNREACHABLE">
<h3>SERVER_UNREACHABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">SERVER_UNREACHABLE</span></div>
<div class="block"><p>Server unreachable.</p></div>
</section>
</li>
<li>
<section class="detail" id="FORBIDDEN">
<h3>FORBIDDEN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">FORBIDDEN</span></div>
<div class="block"><p>The credentials given do not provide access to the resource requested.</p></div>
</section>
</li>
<li>
<section class="detail" id="EXCEEDED_USAGE_LIMIT">
<h3>EXCEEDED_USAGE_LIMIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">EXCEEDED_USAGE_LIMIT</span></div>
<div class="block"><p>Credentials exceeded the allowed requests limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_FAILED">
<h3>OPERATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">OPERATION_FAILED</span></div>
<div class="block"><p>Operation failed due to an internal error.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_CANCELLED">
<h3>OPERATION_CANCELLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">OPERATION_CANCELLED</span></div>
<div class="block"><p>Operation cancelled.</p></div>
</section>
</li>
<li>
<section class="detail" id="TIMED_OUT">
<h3>TIMED_OUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">TIMED_OUT</span></div>
<div class="block"><p>The request timed out.</p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE">
<h3>OFFLINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">OFFLINE</span></div>
<div class="block"><p>The device does not have an internet connection.</p></div>
</section>
</li>
<li>
<section class="detail" id="QUERY_TOO_LONG">
<h3>QUERY_TOO_LONG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">QUERY_TOO_LONG</span></div>
<div class="block"><p>Query is too long, max. size is 300 characters.</p></div>
</section>
</li>
<li>
<section class="detail" id="FILTER_TOO_LONG">
<h3>FILTER_TOO_LONG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">FILTER_TOO_LONG</span></div>
<div class="block"><p>Filter is too long, max. size is 300 characters.</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_AUTHENTICATION_FAILED">
<h3>PROXY_AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span></div>
<div class="block"><p>Proxy is not authenticated. Check your proxy credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_SERVER_UNREACHABLE">
<h3>PROXY_SERVER_UNREACHABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span></div>
<div class="block"><p>Proxy server unreachable.</p></div>
</section>
</li>
<li>
<section class="detail" id="QUERY_EMPTY">
<h3>QUERY_EMPTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">QUERY_EMPTY</span></div>
<div class="block"><p>Empty query</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_AREA">
<h3>INVALID_AREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">INVALID_AREA</span></div>
<div class="block"><p>Box or circle area of query is invalid</p></div>
</section>
</li>
<li>
<section class="detail" id="FILTER_EMPTY">
<h3>FILTER_EMPTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">FILTER_EMPTY</span></div>
<div class="block"><p>Filter is empty</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_CORRIDOR_POLYLINE">
<h3>INVALID_CORRIDOR_POLYLINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">INVALID_CORRIDOR_POLYLINE</span></div>
<div class="block"><p>Corridor area polyline size is less than 2 points</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_URL">
<h3>INVALID_URL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">INVALID_URL</span></div>
<div class="block"><p>Url is invalid</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_CUSTOM_OPTION_FORMAT">
<h3>INVALID_CUSTOM_OPTION_FORMAT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">INVALID_CUSTOM_OPTION_FORMAT</span></div>
<div class="block"><p>Custom options are set in an invalid format in the query</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_TRUCK_CLASS">
<h3>INVALID_TRUCK_CLASS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">INVALID_TRUCK_CLASS</span></div>
<div class="block"><p>Light truck class is passed in the filter</p></div>
</section>
</li>
<li>
<section class="detail" id="BAD_REQUEST">
<h3>BAD_REQUEST</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">BAD_REQUEST</span></div>
<div class="block"><p>Bad network request</p></div>
</section>
</li>
<li>
<section class="detail" id="MAP_NOT_READY">
<h3>MAP_NOT_READY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">MAP_NOT_READY</span></div>
<div class="block"><p>Offline map data is incomplete for the requested operation.
 Regions are not downloaded or are in the <code>Pending</code> state.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="LAYERS_NOT_DOWNLOADED">
<h3>LAYERS_NOT_DOWNLOADED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">LAYERS_NOT_DOWNLOADED</span></div>
<div class="block"><p>Downloaded regions missing <a href="sdk-for-android-navigate-layerconfiguration.feature#OFFLINE_SEARCH_GLOBAL"><code>LayerConfiguration.Feature.OFFLINE_SEARCH_GLOBAL</code></a>
 feature. Update or redownload regions with enabled feature.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
