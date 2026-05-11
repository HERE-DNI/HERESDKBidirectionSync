---
title: "Untitled"
slug: "sdk-for-android-explore-usagestats-networkstats"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- UsageStats.NetworkStats.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li>Method</li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.core.engine</a></div>
<h1 class="title" title="Class UsageStats.NetworkStats">Class UsageStats.NetworkStats</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.engine.UsageStats.NetworkStats</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-usagestats" title="class in com.here.sdk.core.engine">UsageStats</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">UsageStats.NetworkStats</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Provides network statistics in bytes per method.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#methodCall">methodCall</a></code></div>
<div class="col-last even-row-color">
<div class="block">Name or description of the method being called.</div>
</div>
<div class="col-first odd-row-color"><code>long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#receivedBytes">receivedBytes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of bytes received from the network.</div>
</div>
<div class="col-first even-row-color"><code>long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#requestCounter">requestCounter</a></code></div>
<div class="col-last even-row-color">
<div class="block">Amount of calls for particular family of methodCall.</div>
</div>
<div class="col-first odd-row-color"><code>long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#sentBytes">sentBytes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of bytes sent over the network.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(long,long,java.lang.String,long)">NetworkStats</a><wbr/>(long sentBytes,
 long receivedBytes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> methodCall,
 long requestCounter)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="sentBytes">
<h3>sentBytes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">sentBytes</span></div>
<div class="block"><p>Number of bytes sent over the network.</p></div>
</section>
</li>
<li>
<section class="detail" id="receivedBytes">
<h3>receivedBytes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">receivedBytes</span></div>
<div class="block"><p>Number of bytes received from the network.</p></div>
</section>
</li>
<li>
<section class="detail" id="methodCall">
<h3>methodCall</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">methodCall</span></div>
<div class="block"><p>Name or description of the method being called.</p></div>
</section>
</li>
<li>
<section class="detail" id="requestCounter">
<h3>requestCounter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">requestCounter</span></div>
<div class="block"><p>Amount of calls for particular family of methodCall.
 methodCall in this case is considered as base request,
 additional query params are ignored, all calculated as one request.
 e.g. https://search.hereapi.com/someparams and https://search.hereapi.com/someparams2
 will be considered as 1 methodCall, and requestCounter is 2.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(long,long,java.lang.String,long)">
<h3>NetworkStats</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NetworkStats</span><wbr/><span class="parameters">(long sentBytes,
 long receivedBytes,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> methodCall,
 long requestCounter)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sentBytes</code> - <p>Number of bytes sent over the network.</p></dd>
<dd><code>receivedBytes</code> - <p>Number of bytes received from the network.</p></dd>
<dd><code>methodCall</code> - <p>Name or description of the method being called.</p></dd>
<dd><code>requestCounter</code> - <p>Amount of calls for particular family of methodCall.
 methodCall in this case is considered as base request,
 additional query params are ignored, all calculated as one request.
 e.g. https://search.hereapi.com/someparams and https://search.hereapi.com/someparams2
 will be considered as 1 methodCall, and requestCounter is 2.</p></dd>
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
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
