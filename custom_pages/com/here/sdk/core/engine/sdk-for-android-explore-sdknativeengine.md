---
title: "SDKNativeEngine (API Reference)"
slug: "sdk-for-android-explore-sdknativeengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SDKNativeEngine.html -->
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
<li><a href="../../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../../index-all.html">Index</a></li>
<li><a href="../../../../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.core.engine</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../NativeBase.html" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.core.engine.SDKNativeEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SDKNativeEngine</span>
<span class="extends-implements">extends <a href="../../../NativeBase.html" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Holds internal services and configurations needed by various HERE SDK modules.
 <p>You can initialize the HERE SDK in two ways:
 <ul>
<li>Create a shared instance of the <code>SDKNativeEngine</code> with <code>SDKNativeEngine.makeSharedInstance()</code>.</li>
<li>Create individual instances of the <code>SDKNativeEngine</code> via <code>SDKNativeEngine()</code>. Note that this does not automatically set a shared instance.</li>
</ul></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SDKNativeEngine.PurgeMemoryStrategy.html" title="enum class in com.here.sdk.core.engine">SDKNativeEngine.PurgeMemoryStrategy</a></code></div>
<div class="col-last even-row-color">
<div class="block">Enum representing a strategy to flush memory caches.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(android.content.Context,com.here.sdk.core.engine.SDKOptions)">SDKNativeEngine</a><wbr/>(android.content.Context androidContext,
 <a href="SDKOptions.html" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</code></div>
<div class="col-last even-row-color">
<div class="block">Makes a new instance of SDKNativeEngine using supplied options.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearPersistentUsageStats()">clearPersistentUsageStats</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear persistent storage for the HERE SDK <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearUsageStatsCache()">clearUsageStatsCache</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear cache for the HERE SDK <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stops pending requests and closes open files and databases .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enableUsageStats(boolean)">enableUsageStats</a><wbr/>(boolean enabled)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enable or disable <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> for the HERE SDK.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)">getDeviceId</a><wbr/>(<a href="DeviceIdCallback.html" title="interface in com.here.sdk.core.engine">DeviceIdCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The unique identifier assigned to the device for this application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SDKOptions.html" title="class in com.here.sdk.core.engine">SDKOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the options used by this instance of <a href="SDKNativeEngine.html" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../ParameterConfiguration.html" title="class in com.here.sdk.core">ParameterConfiguration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameterConfig()">getParameterConfig</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the configuration for default values of parameters used in the HERE SDK.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="PassThroughFeature.html" title="enum class in com.here.sdk.core.engine">PassThroughFeature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPassThroughFeatures()">getPassThroughFeatures</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the pass through features.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProxySettings.html" title="class in com.here.sdk.core.engine">ProxySettings</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProxySettings()">getProxySettings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current proxy settings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="UsageStats.html" title="class in com.here.sdk.core.engine">UsageStats</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSdkUsageStats()">getSdkUsageStats</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a list of usage statistics for all available HERE SDK features.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SDKNativeEngine.html" title="class in com.here.sdk.core.engine">SDKNativeEngine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedInstance()">getSharedInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
 engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOfflineMode()">isOfflineMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current offline mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#makeSharedInstance(android.content.Context,com.here.sdk.core.engine.SDKOptions)">makeSharedInstance</a><wbr/>(android.content.Context androidContext,
 <a href="SDKOptions.html" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a new instance of this class using the supplied options and stores it as shared instance
 see <a href="#getSharedInstance()"><code>getSharedInstance()</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)">purgeMemoryCaches</a><wbr/>(<a href="SDKNativeEngine.PurgeMemoryStrategy.html" title="enum class in com.here.sdk.core.engine">SDKNativeEngine.PurgeMemoryStrategy</a> strategy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Releases memory occupied by internal caches.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAccessKeySecret(java.lang.String)">setAccessKeySecret</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> accessKeySecret)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Overrides HERE SDK access key secret with new value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAccessScope(java.lang.String)">setAccessScope</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Overrides the token scope of the HERE SDK with new value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOfflineMode(boolean)">setOfflineMode</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the offline mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setParameterConfig(com.here.sdk.core.ParameterConfiguration)">setParameterConfig</a><wbr/>(<a href="../ParameterConfiguration.html" title="class in com.here.sdk.core">ParameterConfiguration</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the configuration for default values of parameters used in the HERE SDK.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPassThroughFeatures(java.util.Set)">setPassThroughFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="PassThroughFeature.html" title="enum class in com.here.sdk.core.engine">PassThroughFeature</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the pass through features.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProxySettings(com.here.sdk.core.engine.ProxySettings)">setProxySettings</a><wbr/>(<a href="ProxySettings.html" title="class in com.here.sdk.core.engine">ProxySettings</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the proxy settings.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSharedInstance(com.here.sdk.core.engine.SDKNativeEngine)">setSharedInstance</a><wbr/>(<a href="SDKNativeEngine.html" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
 engine.</div>
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
<section class="detail" id="&lt;init&gt;(android.content.Context,com.here.sdk.core.engine.SDKOptions)">
<h3>SDKNativeEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SDKNativeEngine</span><wbr/><span class="parameters">(@NonNull
 android.content.Context androidContext,
 @NonNull
 <a href="SDKOptions.html" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span>
                throws <span class="exceptions"><a href="../errors/InstantiationErrorException.html" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Makes a new instance of SDKNativeEngine using supplied options.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>androidContext</code> - <p>The Android context</p></dd>
<dd><code>options</code> - <p>The options for the new engine.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="../errors/InstantiationErrorException.html" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="setAccessKeySecret(java.lang.String)">
<h3>setAccessKeySecret</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAccessKeySecret</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> accessKeySecret)</span></div>
<div class="block"><p>Overrides HERE SDK access key secret with new value.
 The new credentials will be used for new requests.
 <p><strong>Note:</strong>
 This method can be called from any thread.
 Access key ID can be set with constructor of SDKNativeEngine.
 New instance of SDKNativeEngine should be used if a new access key ID is required.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>accessKeySecret</code> - <p>New access key secret.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAccessScope(java.lang.String)">
<h3>setAccessScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAccessScope</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> scope)</span></div>
<div class="block"><p>Overrides the token scope of the HERE SDK with new value.
 A new token will be fetched with the set scope and used for future requests.
 Setting an empty string will fetch a token for the global scope.
 <p>This method can be called from any thread.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scope</code> - <p>New scope for token</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block"><p>Stops pending requests and closes open files and databases .
 Dispose signal is sent to dependent modules.
 Usage of engine, or dependent modules after calling dispose leads to undefined behavior.
 Please be aware that this method does not clean any type of storage.
 <strong>Note:</strong>
 This method should be called from main thread.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableUsageStats(boolean)">
<h3>enableUsageStats</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableUsageStats</span><wbr/><span class="parameters">(boolean enabled)</span></div>
<div class="block"><p>Enable or disable <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> for the HERE SDK. Defaults to disabled (false). When enabled, <code>SDKNativeEngine.getSdkUsageStats()</code>
 returns actual online data consumption. Note that the flag does not cancel pending requests.
 <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> can be enabled or disabled at any time.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enabled</code> - <p>True, if UsageStats are enabled.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeSharedInstance(android.content.Context,com.here.sdk.core.engine.SDKOptions)">
<h3>makeSharedInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">makeSharedInstance</span><wbr/><span class="parameters">(@NonNull
 android.content.Context androidContext,
 @NonNull
 <a href="SDKOptions.html" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span>
                               throws <span class="exceptions"><a href="../errors/InstantiationErrorException.html" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Makes a new instance of this class using the supplied options and stores it as shared instance
 see <a href="#getSharedInstance()"><code>getSharedInstance()</code></a>. If there was a previously shared instance
 then it's disposed (so there is no need to call <a href="#dispose()"><code>dispose()</code></a> on app side) before the new instance is created.
 <p><strong>Note:</strong> The HERE SDK is not guaranteed to be thread safe and it is required to make calls
 to the SDK - including this one - from the main thread.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>androidContext</code> - <p>The Android context</p></dd>
<dd><code>options</code> - <p>The options for the new engine.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="../errors/InstantiationErrorException.html" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearPersistentUsageStats()">
<h3>clearPersistentUsageStats</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearPersistentUsageStats</span>()</div>
<div class="block"><p>Clear persistent storage for the HERE SDK <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="clearUsageStatsCache()">
<h3>clearUsageStatsCache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearUsageStatsCache</span>()</div>
<div class="block"><p>Clear cache for the HERE SDK <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)">
<h3>purgeMemoryCaches</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">purgeMemoryCaches</span><wbr/><span class="parameters">(@NonNull
 <a href="SDKNativeEngine.PurgeMemoryStrategy.html" title="enum class in com.here.sdk.core.engine">SDKNativeEngine.PurgeMemoryStrategy</a> strategy)</span></div>
<div class="block"><p>Releases memory occupied by internal caches.
 Purging caches reduces memory footprint of application and may temporary reduce performance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>strategy</code> - <p>Option to control how much memory caches will be purged.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)">
<h3>getDeviceId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getDeviceId</span><wbr/><span class="parameters">(@NonNull
 <a href="DeviceIdCallback.html" title="interface in com.here.sdk.core.engine">DeviceIdCallback</a> callback)</span></div>
<div class="block"><p>The unique identifier assigned to the device for this application.
 This device ID is primarily used for tracking Monthly Active Users (MAUs).</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="SDKOptions.html" title="class in com.here.sdk.core.engine">SDKOptions</a></span> <span class="element-name">getOptions</span>()</div>
<div class="block"><p>Gets the options used by this instance of <a href="SDKNativeEngine.html" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Options used by this instance of <a href="SDKNativeEngine.html" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedInstance()">
<h3>getSharedInstance</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SDKNativeEngine.html" title="class in com.here.sdk.core.engine">SDKNativeEngine</a></span> <span class="element-name">getSharedInstance</span>()</div>
<div class="block"><p>Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
 engine.
 <p>This is automatically set as a part of the SDK initialization process.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
     engine.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSharedInstance(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>setSharedInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSharedInstance</span><wbr/><span class="parameters">(@Nullable
 <a href="SDKNativeEngine.html" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> value)</span></div>
<div class="block"><p>Sets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
 engine.
 <p>This is automatically set as a part of the SDK initialization process.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
     engine.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOfflineMode()">
<h3>isOfflineMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOfflineMode</span>()</div>
<div class="block"><p>Gets the current offline mode.
 <p>Sets offline mode for the HERE SDK to offline or online.
 Defaults to false, which means the HERE SDK uses an online connection.
 When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
 See <a href="#getPassThroughFeatures()"><code>getPassThroughFeatures()</code></a>.
 Note that the flag does not cancel pending requests.
 The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
 needs to be enabled via <a href="SDKOptions.html#offlineMode"><code>SDKOptions.offlineMode</code></a>.
 Initialization of the HERE SDK itself does not require an internet connection.
 Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.
 <p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The offline mode.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOfflineMode(boolean)">
<h3>setOfflineMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOfflineMode</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets the offline mode.
 <p>Sets offline mode for the HERE SDK to offline or online.
 Defaults to false, which means the HERE SDK uses an online connection.
 When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
 See <a href="#getPassThroughFeatures()"><code>getPassThroughFeatures()</code></a>.
 Note that the flag does not cancel pending requests.
 The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
 needs to be enabled via <a href="SDKOptions.html#offlineMode"><code>SDKOptions.offlineMode</code></a>.
 Initialization of the HERE SDK itself does not require an internet connection.
 Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.
 <p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The offline mode.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPassThroughFeatures()">
<h3>getPassThroughFeatures</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="PassThroughFeature.html" title="enum class in com.here.sdk.core.engine">PassThroughFeature</a>&gt;</span> <span class="element-name">getPassThroughFeatures</span>()</div>
<div class="block"><p>Gets the pass through features.
 <p>Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
 Pass through features can be updated at any time.
 When offline mode is disabled, existing pass through features will be removed.
 These needs to be set again when you enable offline mode next time.
 By default, reporting of HERE SDK <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> will be enabled when at least one pass-through feature is set.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The pass through features.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPassThroughFeatures(java.util.Set)">
<h3>setPassThroughFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPassThroughFeatures</span><wbr/><span class="parameters">(@Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="PassThroughFeature.html" title="enum class in com.here.sdk.core.engine">PassThroughFeature</a>&gt; value)</span></div>
<div class="block"><p>Sets the pass through features.
 <p>Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
 Pass through features can be updated at any time.
 When offline mode is disabled, existing pass through features will be removed.
 These needs to be set again when you enable offline mode next time.
 By default, reporting of HERE SDK <a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> will be enabled when at least one pass-through feature is set.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The pass through features.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameterConfig()">
<h3>getParameterConfig</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../ParameterConfiguration.html" title="class in com.here.sdk.core">ParameterConfiguration</a></span> <span class="element-name">getParameterConfig</span>()</div>
<div class="block"><p>Gets the configuration for default values of parameters used in the HERE SDK.
 <p><strong>Note:</strong> This feature is in beta state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Configuration for default values of parameters used in the HERE SDK.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParameterConfig(com.here.sdk.core.ParameterConfiguration)">
<h3>setParameterConfig</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setParameterConfig</span><wbr/><span class="parameters">(@NonNull
 <a href="../ParameterConfiguration.html" title="class in com.here.sdk.core">ParameterConfiguration</a> value)</span></div>
<div class="block"><p>Sets the configuration for default values of parameters used in the HERE SDK.
 <p><strong>Note:</strong> This feature is in beta state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Configuration for default values of parameters used in the HERE SDK.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProxySettings()">
<h3>getProxySettings</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="ProxySettings.html" title="class in com.here.sdk.core.engine">ProxySettings</a></span> <span class="element-name">getProxySettings</span>()</div>
<div class="block"><p>Gets the current proxy settings.
 <p>Defaults to (<code>null</code>), which indicates proxy is not enabled.
 When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
 Pass (<code>null</code>) to indicate that proxy should be disabled.
 If proxy is necessary from the start then it's recommended to use <a href="NetworkSettings.html#proxySettings"><code>NetworkSettings.proxySettings</code></a> in <a href="SDKOptions.html#networkSettings"><code>SDKOptions.networkSettings</code></a>.
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProxySettings(com.here.sdk.core.engine.ProxySettings)">
<h3>setProxySettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProxySettings</span><wbr/><span class="parameters">(@Nullable
 <a href="ProxySettings.html" title="class in com.here.sdk.core.engine">ProxySettings</a> value)</span></div>
<div class="block"><p>Sets the proxy settings.
 <p>Defaults to (<code>null</code>), which indicates proxy is not enabled.
 When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
 Pass (<code>null</code>) to indicate that proxy should be disabled.
 If proxy is necessary from the start then it's recommended to use <a href="NetworkSettings.html#proxySettings"><code>NetworkSettings.proxySettings</code></a> in <a href="SDKOptions.html#networkSettings"><code>SDKOptions.networkSettings</code></a>.
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSdkUsageStats()">
<h3>getSdkUsageStats</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="UsageStats.html" title="class in com.here.sdk.core.engine">UsageStats</a>&gt;</span> <span class="element-name">getSdkUsageStats</span>()</div>
<div class="block"><p>Gets a list of usage statistics for all available HERE SDK features.
 <p><a href="UsageStats.html" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> has cache and persistent storage. Reads from the persistent storage happen on <code>SDKNativeEngine</code> creation step.
 Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Gets a list of usage statistics for all available HERE SDK features.</p></dd>
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
