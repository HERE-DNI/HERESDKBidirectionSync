---
title: "Authentication (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-authentication"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Authentication.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.core.Authentication</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Authentication</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Use the authentication class to authenticate and retrieve a secure token that
 can be used with other HERE services.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-authenticationdata" title="class in com.here.sdk.core">AuthenticationData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-authentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine)">authenticate</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkNativeEngine)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Uses the authentication service that is connected to the given SDK engine to authenticate and
 retrieve a secure token.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-authentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.core.AuthenticationCallback)">authenticate</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkNativeEngine,
 <a href="sdk-for-android-navigate-authenticationcallback" title="interface in com.here.sdk.core">AuthenticationCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Uses the authentication service that is connected to the given SDK engine to authenticate and
 retrieve a secure token.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="authenticate(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.core.AuthenticationCallback)">
<h3>authenticate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">authenticate</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkNativeEngine,
 @NonNull
 <a href="sdk-for-android-navigate-authenticationcallback" title="interface in com.here.sdk.core">AuthenticationCallback</a> callback)</span></div>
<div class="block"><p>Uses the authentication service that is connected to the given SDK engine to authenticate and
 retrieve a secure token. This method operates asynchronously.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkNativeEngine</code> - <p>The SDK engine instance.</p></dd>
<dd><code>callback</code> - <p>Callback to retrieve an authentication token on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="authenticate(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>authenticate</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-authenticationdata" title="class in com.here.sdk.core">AuthenticationData</a></span> <span class="element-name">authenticate</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkNativeEngine)</span>
                                       throws <span class="exceptions"><a href="sdk-for-android-navigate-authenticationexception" title="class in com.here.sdk.core">AuthenticationException</a></span></div>
<div class="block"><p>Uses the authentication service that is connected to the given SDK engine to authenticate and
 retrieve a secure token. This method operates synchronously.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkNativeEngine</code> - <p>The SDK engine instance.</p></dd>
<dt>Returns:</dt>
<dd><p>Authentication data.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-authenticationexception" title="class in com.here.sdk.core">AuthenticationException</a></code> - <p>Authentication exception that describes the error.</p></dd>
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
