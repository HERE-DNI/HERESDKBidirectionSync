---
title: "IsolineRoutingEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-isolineroutingengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- IsolineRoutingEngine.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.IsolineRoutingEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">IsolineRoutingEngine</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Use the IsolineRoutingEngine to calculate a reachable area from a center point.
 The calculation is done asynchronously and requires an
 online connection.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E()">IsolineRoutingEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">IsolineRoutingEngine</a><wbr/>(<a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of IsolineRoutingEngine.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings)">IsolineRoutingEngine</a><wbr/>(<a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of RoutingEngine.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.routing.RoutingConnectionSettings)">IsolineRoutingEngine</a><wbr/>(<a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of RoutingEngine.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#calculateIsoline(com.here.sdk.routing.Waypoint,com.here.sdk.routing.IsolineOptions,com.here.sdk.routing.CalculateIsolineCallback)">calculateIsoline</a><wbr/>(<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> center,
 <a href="sdk-for-android-explore-isolineoptions" title="class in com.here.sdk.routing">IsolineOptions</a> isolineOptions,
 <a href="sdk-for-android-explore-calculateisolinecallback" title="interface in com.here.sdk.routing">CalculateIsolineCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates isolines to indicate the reachable area from a center point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setCustomOption(java.lang.String,java.lang.String)">setCustomOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a custom option for routing backend queries.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>IsolineRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span>()
                     throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.RoutingConnectionSettings)">
<h3>IsolineRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</span>
                     throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of RoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connectionSettings</code> - <p>Settings for the route calculation.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings)">
<h3>IsolineRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</span>
                     throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of RoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dd><code>connectionSettings</code> - <p>Settings for the route calculation.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>IsolineRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                     throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of IsolineRoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
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
<section class="detail" id="calculateIsoline(com.here.sdk.routing.Waypoint,com.here.sdk.routing.IsolineOptions,com.here.sdk.routing.CalculateIsolineCallback)">
<h3>calculateIsoline</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateIsoline</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> center,
 @NonNull
 <a href="sdk-for-android-explore-isolineoptions" title="class in com.here.sdk.routing">IsolineOptions</a> isolineOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateisolinecallback" title="interface in com.here.sdk.routing">CalculateIsolineCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates isolines to indicate the reachable area from a center point.
 This finds all destinations that can be reached in a specific amount of time,
 a maximum travel distance, or even the charge level available in an electric vehicle.
 The result is a polygon area where each point is reachable within the provided limit.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>center</code> - <p>Center point from which isolines are calculated.
     At minimum, the waypoint must contain the coordinates as point of origin.</p></dd>
<dd><code>isolineOptions</code> - <p>Options for isoline calculation.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after isoline calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomOption(java.lang.String,java.lang.String)">
<h3>setCustomOption</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">setCustomOption</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>Sets a custom option for routing backend queries.
 The custom option is applied to all the queries that <code>IsolineRoutingEngine</code> performs.
 For a complete list of available parameter names and their valid values, refer to
 <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Routing API v8</a>.
 <strong>Note:</strong> It's easy to set a wrong option that makes queries invalid,
 so make sure you read and understand the backend documentation.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.
     The option name should't duplicate option names that SDK creates by itself for usage in the query,
     otherwise the query will callback with the error <code>RoutingError.INTERNAL_ERROR</code>.</p></dd>
<dd><code>value</code> - <p>An option value. If the value is <code>null</code>, the option will be removed. The option value must be a non-empty string.</p></dd>
<dt>Returns:</dt>
<dd><p>An optional error of setting the option. It's <code>null</code> if the option has been set successfully.
     It's <code>RoutingError.INVALID_PARAMETER</code> if the input name and/or value haven't passed internal validation.</p></dd>
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
