---
title: "AdministrativeRulesLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AdministrativeRulesLoader.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapdata.AdministrativeRulesLoader</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AdministrativeRulesLoader</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Provides the interface for the access to the administrative rules available
 for a country or a state in the local OCM map. Please be aware that the methods within this
 classload map data synchronously. In the event of absent data in the disk cache, the data
 will be retrieved from the remote server. To mitigate the potential freezing of the calling
 thread, it is advisable to proactively prefetch map data around the working area.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader#%3Cinit%3E()">AdministrativeRulesLoader</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerulesloader#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">AdministrativeRulesLoader</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>AdministrativeRulesLoader</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AdministrativeRulesLoader</span>()
                          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>AdministrativeRulesLoader</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AdministrativeRulesLoader</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getStateCodes(com.here.sdk.core.CountryCode)">
<h3>getStateCodes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">getStateCodes</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode)</span>
                           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div className="block"><p>Synchronously loads the list of state codes from a specified country for which
 administrative rules are availabe. These state codes can then be used to get specific
 administrative rules for a specified state using the <code>get_administrative_rules()</code> method.
 Returns a list with all the state codes available in the country. In case the country has no
 states, the list will be empty.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>countryCode</code> - <p>The country code for which the state codes are going to be retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of state codes present in the country for which administrative rules
     are available.
     Throws if it's not possible to return the list of state codes.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why the list of state codes was not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAdministrativeRules(com.here.sdk.core.CountryCode,java.lang.String)">
<h3>getAdministrativeRules</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></span> <span className="element-name">getAdministrativeRules</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateCode)</span>
                                           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div className="block"><p>Synchronously load the administrative rules for the specified country and state.
 <strong>Note:</strong> The <code>state_code</code> parameter can be set to <code>null</code>. In this case, even if the country has multiple states, each with
 their own administrative rules, an <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> object will be returned, containing the administrative
 rules valid for the entire country. These rules can however be overwritten by the state rules when the driver is in that
 specific state, so it is recommended to always retrieve the rules for a specific state for higher accuracy.
 Returns an <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> object which contains the administrative rules for the specified country and
 state.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>countryCode</code> - <p>The country code for which the administrative rules will be retrieved.</p></dd>
<dd><code>stateCode</code> - <p>The state name for which the administrative rules will be received. It can be <code>null</code>.</p></dd>
<dt>Returns:</dt>
<dd><p>Requested administrative rules for the country and the state specified.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why the administrative rules were not retrieved.</p></dd>
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
