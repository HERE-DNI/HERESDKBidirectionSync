---
title: "WarnerEngine (API Reference)"
slug: "sdk-for-android-navigate-warnerengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- WarnerEngine.html -->
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
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.warner</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.warner.WarnerEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">WarnerEngine</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></span></div>
<div class="block"><p>Provides the core functionality for generating and managing navigation warnings.
 <p><code>WarnerEngine</code> processes Electronic Horizon data and determines when various types
 of warnings should be issued. It is used with <a href="sdk-for-android-navigate-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a>,
 which supply the road topology and positional updates required for warning evaluation.
 <p>The engine monitors enabled warning types and notifies registered listeners when new warnings become available.
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></p></p></p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.navigation.WallClock,java.util.List)">WarnerEngine</a><wbr/>(<a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-navigation-wallclock" title="interface in com.here.sdk.navigation">WallClock</a> wallClock,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,java.util.List)">WarnerEngine</a><wbr/>(<a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.List)">WarnerEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</code></div>
<div class="col-last even-row-color">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCustomWarningProvider(com.here.sdk.warner.CustomWarningProvider,com.here.sdk.mapdata.SegmentDataLoaderOptions)">addCustomWarningProvider</a><wbr/>(<a href="sdk-for-android-navigate-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider,
 <a href="sdk-for-android-navigate-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> segmentDataLoaderOptions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers a custom warning provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addEnabledWarnings(java.util.List)">addEnabledWarnings</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given warning types to the set of warnings monitored by the engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addWarningListener(com.here.sdk.warner.WarningListener)">addWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers a listener that will receive warning notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCustomWarningProviders()">clearCustomWarningProviders</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters all custom warning providers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#finalizeGivenWarnings()">finalizeGivenWarnings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks all currently active warnings as passed (<code>DistanceType.PASSED</code>), notifies all
 registered <a href="sdk-for-android-navigate-warninglistener" title="interface in com.here.sdk.warner"><code>WarningListener</code></a> instances on the main thread, and then clears these
 warnings from their corresponding registries by invoking the appropriate<code>WarningsRegistry.clear&lt;Type&gt;</code> methods.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomWarningNotificationDistances(int)">getCustomWarningNotificationDistances</a><wbr/>(int customWarningType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the warning notification distances for the specified custom warning type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnabledWarnings()">getEnabledWarnings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the current list of enabled warning types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimingProfile()">getTimingProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently configured <a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">getWarningNotificationDistances</a><wbr/>(<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the warning notification distances for the requested warning type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWarningOptions()">getWarningOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently configured <a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner"><code>WarningOptions</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-warningsregistry" title="class in com.here.sdk.warner">WarningsRegistry</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWarningsRegistry()">getWarningsRegistry</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the centralized access point for retrieving full metadata of any supported
 warning category (e.g., safety cameras, truck restrictions, etc.).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">onElectronicHorizonUpdated</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizon-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode,
 <a href="sdk-for-android-navigate-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called whenever the electronic horizon subsystem produces:
 
 a new update,
 an error,
 </div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCustomWarningProvider(com.here.sdk.warner.CustomWarningProvider)">removeCustomWarningProvider</a><wbr/>(<a href="sdk-for-android-navigate-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters a custom warning provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeEnabledWarnings(java.util.List)">removeEnabledWarnings</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the given warning types from the set of warnings monitored by the engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeWarningListener(com.here.sdk.warner.WarningListener)">removeWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters a previously added warning listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomWarningNotificationDistances(int,com.here.sdk.navigation.WarningNotificationDistances)">setCustomWarningNotificationDistances</a><wbr/>(int customWarningType,
 <a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the warning notification distances for the specified custom warning type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnabledWarnings(java.util.List)">setEnabledWarnings</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replaces the current set of enabled warning types with the provided list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimingProfile(com.here.sdk.navigation.TimingProfile)">setTimingProfile</a><wbr/>(<a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a> of the current position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">setWarningNotificationDistances</a><wbr/>(<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 <a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the warning notification distances for the specified warning type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWarningOptions(com.here.sdk.warner.WarningOptions)">setWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner"><code>WarningOptions</code></a> and updates the configuration for all the warners.</div>
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
<section class="detail" id="&lt;init&gt;(java.util.List)">
<h3>WarnerEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">WarnerEngine</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</span>
             throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enabledWarnings</code> - <p>The list of warning types that should be monitored and processed
     by the engine. Only warnings of these types will be generated.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,java.util.List)">
<h3>WarnerEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">WarnerEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</span>
             throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A <code>SDKEngine</code> instance.</p></dd>
<dd><code>enabledWarnings</code> - <p>The list of warning types that should be monitored and processed
     by the engine. Only warnings of these types will be generated.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.navigation.WallClock,java.util.List)">
<h3>WarnerEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">WarnerEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-navigation-wallclock" title="interface in com.here.sdk.navigation">WallClock</a> wallClock,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</span>
             throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A <code>SDKEngine</code> instance.</p></dd>
<dd><code>wallClock</code> - <p>A <code>WallClock</code> instance.</p></dd>
<dd><code>enabledWarnings</code> - <p>The list of warning types that should be monitored and processed
     by the engine. Only warnings of these types will be generated.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="addEnabledWarnings(java.util.List)">
<h3>addEnabledWarnings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addEnabledWarnings</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</span></div>
<div class="block"><p>Adds the given warning types to the set of warnings monitored by the engine.
 <p>After this call, the engine will begin generating warnings for all
 types included in <code>warningTypes</code>, in addition to those that are already enabled.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningTypes</code> - <p>Warning types to be added to the engine's active monitoring set.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeEnabledWarnings(java.util.List)">
<h3>removeEnabledWarnings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeEnabledWarnings</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</span></div>
<div class="block"><p>Removes the given warning types from the set of warnings monitored by the engine.
 <p>After this call, the engine will stop generating warnings for all
 types included in <code>warningTypes</code>, while other enabled types remain unaffected.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningTypes</code> - <p>Warning types to be removed from the engine's active monitoring set.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnabledWarnings(java.util.List)">
<h3>setEnabledWarnings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnabledWarnings</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</span></div>
<div class="block"><p>Replaces the current set of enabled warning types with the provided list.
 <p>After this call, the engine will monitor and generate warnings
 only for types included in <code>warningTypes</code>.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningTypes</code> - <p>The complete new set of warning types the engine should track.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnabledWarnings()">
<h3>getEnabledWarnings</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt;</span> <span class="element-name">getEnabledWarnings</span>()</div>
<div class="block"><p>Returns the current list of enabled warning types.
 If the WarnerEngine was retrieved from the <code>Navigator</code>, it will also contain
 all the warnings enabled for which listeners are set.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The currect list instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addWarningListener(com.here.sdk.warner.WarningListener)">
<h3>addWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addWarningListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</span></div>
<div class="block"><p>Registers a listener that will receive warning notifications.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningListener</code> - <p>The listener instance that should be notified when new warnings are generated.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeWarningListener(com.here.sdk.warner.WarningListener)">
<h3>removeWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeWarningListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</span></div>
<div class="block"><p>Unregisters a previously added warning listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningListener</code> - <p>The listener instance that should no longer receive warning notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarningsRegistry()">
<h3>getWarningsRegistry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-warningsregistry" title="class in com.here.sdk.warner">WarningsRegistry</a></span> <span class="element-name">getWarningsRegistry</span>()</div>
<div class="block"><p>Returns the centralized access point for retrieving full metadata of any supported
 warning category (e.g., safety cameras, truck restrictions, etc.).
 <a href="sdk-for-android-navigate-warningsregistry" title="class in com.here.sdk.warner"><code>WarningsRegistry</code></a> class exposes getter methods, each returning the detailed warning object for the given identifier.
 Use this getter to look up complete warning information by its id, as provided through <code>WarningListener.onWarning</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The centralized <a href="sdk-for-android-navigate-warningsregistry" title="class in com.here.sdk.warner"><code>WarningsRegistry</code></a> instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">
<h3>getWarningNotificationDistances</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getWarningNotificationDistances</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span></div>
<div class="block"><p>Returns the warning notification distances for the requested warning type.
 <p><strong>Note</strong>: <a href="sdk-for-android-navigate-navigation-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a> is not a valid value for this method.
 Use <a href="#getCustomWarningNotificationDistances(int)"><code>getCustomWarningNotificationDistances(int)</code></a> to retrieve distances for a specific
 custom warning type.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the notification distances will be returned.
     Must not be <a href="sdk-for-android-navigate-navigation-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a>.</p></dd>
<dt>Returns:</dt>
<dd><p>The warning notification distances for the given <code>warningType</code>.
     If <code>warningType</code> is <a href="sdk-for-android-navigate-navigation-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a>, a default
     <a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation"><code>WarningNotificationDistances</code></a> value is returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">
<h3>setWarningNotificationDistances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setWarningNotificationDistances</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 @NonNull
 <a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span></div>
<div class="block"><p>Sets the warning notification distances for the specified warning type.
 <p><strong>Note</strong>: <a href="sdk-for-android-navigate-navigation-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a> is not a valid value for this method.
 Use <a href="#setCustomWarningNotificationDistances(int,com.here.sdk.navigation.WarningNotificationDistances)"><code>setCustomWarningNotificationDistances(int, com.here.sdk.navigation.WarningNotificationDistances)</code></a> to configure distances for a specific
 custom warning type.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the warning notification distances will be set.
     Must not be <a href="sdk-for-android-navigate-navigation-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a>.</p></dd>
<dd><code>warningNotificationDistances</code> - <p>The warning notification distances to be set for the specified warning type.</p></dd>
<dt>Returns:</dt>
<dd><p>True if the distances were successfully set; false if <code>warningType</code> is
     <a href="sdk-for-android-navigate-navigation-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a> or the options could not be applied.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomWarningNotificationDistances(int)">
<h3>getCustomWarningNotificationDistances</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getCustomWarningNotificationDistances</span><wbr/><span class="parameters">(int customWarningType)</span></div>
<div class="block"><p>Returns the warning notification distances for the specified custom warning type.
 <p>Unlike <a href="#getWarningNotificationDistances(com.here.sdk.navigation.WarningType)"><code>getWarningNotificationDistances(com.here.sdk.navigation.WarningType)</code></a>, which operates on a <a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation"><code>WarningType</code></a>,
 this method targets a specific custom warning category identified by <code>customWarningType</code>,
 as defined in <a href="sdk-for-android-navigate-customwarning#customWarningType"><code>CustomWarning.customWarningType</code></a> and <a href="sdk-for-android-navigate-warning#customWarningType"><code>Warning.customWarningType</code></a>.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>customWarningType</code> - <p>The identifier of the custom warning type for which the
     notification distances are requested.</p></dd>
<dt>Returns:</dt>
<dd><p>The warning notification distances configured for the given <code>customWarningType</code>.
     If no distances have been explicitly set for this type, a default
     <a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation"><code>WarningNotificationDistances</code></a> value is returned.
     <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomWarningNotificationDistances(int,com.here.sdk.navigation.WarningNotificationDistances)">
<h3>setCustomWarningNotificationDistances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setCustomWarningNotificationDistances</span><wbr/><span class="parameters">(int customWarningType,
 @NonNull
 <a href="sdk-for-android-navigate-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span></div>
<div class="block"><p>Sets the warning notification distances for the specified custom warning type.
 <p>Unlike <a href="#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)"><code>setWarningNotificationDistances(com.here.sdk.navigation.WarningType, com.here.sdk.navigation.WarningNotificationDistances)</code></a>, which applies settings to a <a href="sdk-for-android-navigate-navigation-warningtype" title="enum class in com.here.sdk.navigation"><code>WarningType</code></a>,
 this method allows configuring notification distances independently for each custom warning
 category identified by <code>customWarningType</code>, as defined in
 <a href="sdk-for-android-navigate-customwarning#customWarningType"><code>CustomWarning.customWarningType</code></a> and <a href="sdk-for-android-navigate-warning#customWarningType"><code>Warning.customWarningType</code></a>.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>customWarningType</code> - <p>The identifier of the custom warning type for which the
     notification distances should be set.</p></dd>
<dd><code>warningNotificationDistances</code> - <p>The warning notification distances to be applied
     for the specified <code>customWarningType</code>.</p></dd>
<dt>Returns:</dt>
<dd><p>True if the distances were successfully set; false otherwise.
     <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="finalizeGivenWarnings()">
<h3>finalizeGivenWarnings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">finalizeGivenWarnings</span>()</div>
<div class="block"><p>Marks all currently active warnings as passed (<code>DistanceType.PASSED</code>), notifies all
 registered <a href="sdk-for-android-navigate-warninglistener" title="interface in com.here.sdk.warner"><code>WarningListener</code></a> instances on the main thread, and then clears these
 warnings from their corresponding registries by invoking the appropriate<code>WarningsRegistry.clear&lt;Type&gt;</code> methods.
 <p>This method triggers notifications only for enabled warners. Warning processing may
 occur asynchronously unless synchronous mode is enabled.
 <p><strong>Note</strong>: Although each warning type can also be cleared manually via the respective
 <code>WarningsRegistry.clear&lt;Type&gt;()</code> methods, <code>finalizeGivenWarnings()</code> provides a
 unified way to flush all active warnings after they have been reported as
 passed. If this method is not invoked, warnings will continue to accumulate in the
 registry according to the configured warning-generation options.</p></p></p></div>
</section>
</li>
<li>
<section class="detail" id="addCustomWarningProvider(com.here.sdk.warner.CustomWarningProvider,com.here.sdk.mapdata.SegmentDataLoaderOptions)">
<h3>addCustomWarningProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCustomWarningProvider</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider,
 @NonNull
 <a href="sdk-for-android-navigate-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> segmentDataLoaderOptions)</span></div>
<div class="block"><p>Registers a custom warning provider.
 <p>The registered provider participates in warning evaluation and is invoked
 to generate custom warnings based on the current vehicle position.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>customWarningProvider</code> - <p>A provider responsible for generating custom warnings.</p></dd>
<dd><code>segmentDataLoaderOptions</code> - <p>Specifies which data should be loaded by the <code>SegmentDataLoader</code>.
     <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCustomWarningProvider(com.here.sdk.warner.CustomWarningProvider)">
<h3>removeCustomWarningProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCustomWarningProvider</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider)</span></div>
<div class="block"><p>Unregisters a custom warning provider.
 <p>After removal, the provider will no longer participate in warning evaluation
 and will not generate custom warnings.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>customWarningProvider</code> - <p>The provider to be removed.
     <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCustomWarningProviders()">
<h3>clearCustomWarningProviders</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCustomWarningProviders</span>()</div>
<div class="block"><p>Unregisters all custom warning providers.
 <p>After this call, no custom warning providers will participate in warning
 evaluation until new providers are registered.
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></p></p></div>
</section>
</li>
<li>
<section class="detail" id="getWarningOptions()">
<h3>getWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a></span> <span class="element-name">getWarningOptions</span>()</div>
<div class="block"><p>Gets the currently configured <a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner"><code>WarningOptions</code></a>.
 <p>Provides configuration parameters for all the warners.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Options that define warning behavior for all the warners.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWarningOptions(com.here.sdk.warner.WarningOptions)">
<h3>setWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a> value)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-warningoptions" title="class in com.here.sdk.warner"><code>WarningOptions</code></a> and updates the configuration for all the warners.
 <p>Provides configuration parameters for all the warners.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options that define warning behavior for all the warners.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimingProfile()">
<h3>getTimingProfile</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a></span> <span class="element-name">getTimingProfile</span>()</div>
<div class="block"><p>Gets the currently configured <a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a>.
 <p>Configures the base notification thresholds used for delivering
 navigation warnings. The effective thresholds depend on the selected
 <a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a> and may adjust automatically according to
 the current speed limit:
 <ul>
<li>For <a href="sdk-for-android-navigate-navigation-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a>, thresholds apply when the current
 speed limit is above 100 km/h (62 mph).</li>
<li>For <a href="sdk-for-android-navigate-navigation-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a>, thresholds apply when the current
 speed limit is above 60 km/h (37 mph).</li>
<li>For <a href="sdk-for-android-navigate-navigation-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a>, thresholds apply when the current
 speed limit is 60 km/h (37 mph) or below.</li>
</ul>
<p><strong>Note:</strong> Custom threshold values can be set, but these timing-profile rules will still apply.</p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The timing profile that defines when navigation warnings should be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimingProfile(com.here.sdk.navigation.TimingProfile)">
<h3>setTimingProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTimingProfile</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> value)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a> of the current position.
 <p>Configures the base notification thresholds used for delivering
 navigation warnings. The effective thresholds depend on the selected
 <a href="sdk-for-android-navigate-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a> and may adjust automatically according to
 the current speed limit:
 <ul>
<li>For <a href="sdk-for-android-navigate-navigation-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a>, thresholds apply when the current
 speed limit is above 100 km/h (62 mph).</li>
<li>For <a href="sdk-for-android-navigate-navigation-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a>, thresholds apply when the current
 speed limit is above 60 km/h (37 mph).</li>
<li>For <a href="sdk-for-android-navigate-navigation-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a>, thresholds apply when the current
 speed limit is 60 km/h (37 mph) or below.</li>
</ul>
<p><strong>Note:</strong> Custom threshold values can be set, but these timing-profile rules will still apply.</p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The timing profile that defines when navigation warnings should be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">
<h3>onElectronicHorizonUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onElectronicHorizonUpdated</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-electronichorizon-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode,
 @Nullable
 <a href="sdk-for-android-navigate-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</span></div>
<div class="block"><p>Called whenever the electronic horizon subsystem produces:
 <ul>
<li>a new update,</li>
<li>an error,</li>
</ul>
<p>The client must inspect <code>error_code</code> to determine whether the call
 represents an error or a valid update.</p></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-electronichorizon-electronichorizonlistener#onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">onElectronicHorizonUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>errorCode</code> - <p>The error associated with the horizon computation.
     <code>null</code> means no error.</p></dd>
<dd><code>update</code> - <p>The update describing the current electronic horizon state.
     May be <code>null</code> if an update could not be produced.
     <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></p></dd>
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
