---
title: "AdministrativeRulesLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- AdministrativeRulesLoader.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapdata.AdministrativeRulesLoader</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">AdministrativeRulesLoader</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Provides the interface for the access to the administrative rules available
 for a country or a state in the local OCM map. Please be aware that the methods within this
 classload map data synchronously. In the event of absent data in the disk cache, the data
 will be retrieved from the remote server. To mitigate the potential freezing of the calling
 thread, it is advisable to proactively prefetch map data around the working area.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader#%3Cinit%3E()">AdministrativeRulesLoader</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">AdministrativeRulesLoader</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader#getAdministrativeRules(com.here.sdk.core.CountryCode,java.lang.String)">getAdministrativeRules</a><wbr/>(<a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateCode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Synchronously load the administrative rules for the specified country and state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader#getStateCodes(com.here.sdk.core.CountryCode)">getStateCodes</a><wbr/>(<a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Synchronously loads the list of state codes from a specified country for which
 administrative rules are availabe.</div>
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
<h3>AdministrativeRulesLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AdministrativeRulesLoader</span>()
                          throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>AdministrativeRulesLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AdministrativeRulesLoader</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                          throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="getStateCodes(com.here.sdk.core.CountryCode)">
<h3>getStateCodes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStateCodes</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode)</span>
                           throws <span class="exceptions"><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div class="block"><p>Synchronously loads the list of state codes from a specified country for which
 administrative rules are availabe. These state codes can then be used to get specific
 administrative rules for a specified state using the <code>get_administrative_rules()</code> method.
 Returns a list with all the state codes available in the country. In case the country has no
 states, the list will be empty.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>countryCode</code> - <p>The country code for which the state codes are going to be retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of state codes present in the country for which administrative rules
     are available.
     Throws if it's not possible to return the list of state codes.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why the list of state codes was not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdministrativeRules(com.here.sdk.core.CountryCode,java.lang.String)">
<h3>getAdministrativeRules</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></span> <span class="element-name">getAdministrativeRules</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateCode)</span>
                                           throws <span class="exceptions"><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div class="block"><p>Synchronously load the administrative rules for the specified country and state.
 <strong>Note:</strong> The <code>state_code</code> parameter can be set to <code>null</code>. In this case, even if the country has multiple states, each with
 their own administrative rules, an <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> object will be returned, containing the administrative
 rules valid for the entire country. These rules can however be overwritten by the state rules when the driver is in that
 specific state, so it is recommended to always retrieve the rules for a specific state for higher accuracy.
 Returns an <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> object which contains the administrative rules for the specified country and
 state.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>countryCode</code> - <p>The country code for which the administrative rules will be retrieved.</p></dd>
<dd><code>stateCode</code> - <p>The state name for which the administrative rules will be received. It can be <code>null</code>.</p></dd>
<dt>Returns:</dt>
<dd><p>Requested administrative rules for the country and the state specified.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why the administrative rules were not retrieved.</p></dd>
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
