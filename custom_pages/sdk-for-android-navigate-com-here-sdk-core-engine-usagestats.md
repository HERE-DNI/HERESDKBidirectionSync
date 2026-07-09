---
title: "UsageStats (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-usagestats"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- UsageStats.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.engine.UsageStats</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">UsageStats</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-feature" title="enum class in com.here.sdk.core.engine">UsageStats.Feature</a></code></div>
<div className="col-last even-row-color">
<div className="block">Represents the feature enum associated with the gathered usage stats.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats" title="class in com.here.sdk.core.engine">UsageStats.NetworkStats</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Provides network statistics in bytes per method.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-feature" title="enum class in com.here.sdk.core.engine">UsageStats.Feature</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats#feature">feature</a></code></div>
<div className="col-last even-row-color">
<div className="block">Represents the HERE SDK feature associated with the gathered usage statistics.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats" title="class in com.here.sdk.core.engine">UsageStats.NetworkStats</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats#networkStats">networkStats</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Provides network statistics.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats#%3Cinit%3E(java.util.List,com.here.sdk.core.engine.UsageStats.Feature)">UsageStats</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats" title="class in com.here.sdk.core.engine">UsageStats.NetworkStats</a>&gt; networkStats,
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-feature" title="enum class in com.here.sdk.core.engine">UsageStats.Feature</a> feature)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="networkStats">
<h3>networkStats</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats" title="class in com.here.sdk.core.engine">UsageStats.NetworkStats</a>&gt;</span> <span className="element-name">networkStats</span></div>
<div className="block"><p>Provides network statistics.</p></div>
</section>
</li>
<li>
<section className="detail" id="feature">
<h3>feature</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-feature" title="enum class in com.here.sdk.core.engine">UsageStats.Feature</a></span> <span className="element-name">feature</span></div>
<div className="block"><p>Represents the HERE SDK feature associated with the gathered usage statistics.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,com.here.sdk.core.engine.UsageStats.Feature)">
<h3>UsageStats</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">UsageStats</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats" title="class in com.here.sdk.core.engine">UsageStats.NetworkStats</a>&gt; networkStats,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-feature" title="enum class in com.here.sdk.core.engine">UsageStats.Feature</a> feature)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>networkStats</code> - <p>Provides network statistics.</p></dd>
<dd><code>feature</code> - <p>Represents the HERE SDK feature associated with the gathered usage statistics.</p></dd>
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
