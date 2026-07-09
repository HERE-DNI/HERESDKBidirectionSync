---
title: "WarnerEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warnerengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- WarnerEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.warner</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.warner.WarnerEngine</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">WarnerEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></span></div>
<div className="block"><p>Provides the core functionality for generating and managing navigation warnings.
 <code>WarnerEngine</code> processes Electronic Horizon data and determines when various types
 of warnings should be issued. It is used with <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a>,
 which supply the road topology and positional updates required for warning evaluation.
 The engine monitors enabled warning types and notifies registered listeners when new warnings become available.
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


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.navigation.WallClock,java.util.List)">WarnerEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-wallclock" title="interface in com.here.sdk.navigation">WallClock</a> wallClock,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,java.util.List)">WarnerEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine#%3Cinit%3E(java.util.List)">WarnerEngine</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</code></div>
<div className="col-last even-row-color">
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
<section className="detail" id="&lt;init&gt;(java.util.List)">
<h3>WarnerEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">WarnerEngine</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</span>
             throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>enabledWarnings</code> - <p>The list of warning types that should be monitored and processed
     by the engine. Only warnings of these types will be generated.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,java.util.List)">
<h3>WarnerEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">WarnerEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</span>
             throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A <code>SDKEngine</code> instance.</p></dd>
<dd><code>enabledWarnings</code> - <p>The list of warning types that should be monitored and processed
     by the engine. Only warnings of these types will be generated.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.navigation.WallClock,java.util.List)">
<h3>WarnerEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">WarnerEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-wallclock" title="interface in com.here.sdk.navigation">WallClock</a> wallClock,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; enabledWarnings)</span>
             throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A <code>SDKEngine</code> instance.</p></dd>
<dd><code>wallClock</code> - <p>A <code>WallClock</code> instance.</p></dd>
<dd><code>enabledWarnings</code> - <p>The list of warning types that should be monitored and processed
     by the engine. Only warnings of these types will be generated.</p></dd>
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
<section className="detail" id="addEnabledWarnings(java.util.List)">
<h3>addEnabledWarnings</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addEnabledWarnings</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</span></div>
<div className="block"><p>Adds the given warning types to the set of warnings monitored by the engine.
 After this call, the engine will begin generating warnings for all
 types included in <code>warningTypes</code>, in addition to those that are already enabled.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warningTypes</code> - <p>Warning types to be added to the engine's active monitoring set.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeEnabledWarnings(java.util.List)">
<h3>removeEnabledWarnings</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeEnabledWarnings</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</span></div>
<div className="block"><p>Removes the given warning types from the set of warnings monitored by the engine.
 After this call, the engine will stop generating warnings for all
 types included in <code>warningTypes</code>, while other enabled types remain unaffected.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warningTypes</code> - <p>Warning types to be removed from the engine's active monitoring set.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setEnabledWarnings(java.util.List)">
<h3>setEnabledWarnings</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setEnabledWarnings</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt; warningTypes)</span></div>
<div className="block"><p>Replaces the current set of enabled warning types with the provided list.
 After this call, the engine will monitor and generate warnings
 only for types included in <code>warningTypes</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warningTypes</code> - <p>The complete new set of warning types the engine should track.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEnabledWarnings()">
<h3>getEnabledWarnings</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>&gt;</span> <span className="element-name">getEnabledWarnings</span>()</div>
<div className="block"><p>Returns the current list of enabled warning types.
 If the WarnerEngine was retrieved from the <code>Navigator</code>, it will also contain
 all the warnings enabled for which listeners are set.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The currect list instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addWarningListener(com.here.sdk.warner.WarningListener)">
<h3>addWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addWarningListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</span></div>
<div className="block"><p>Registers a listener that will receive warning notifications.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warningListener</code> - <p>The listener instance that should be notified when new warnings are generated.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeWarningListener(com.here.sdk.warner.WarningListener)">
<h3>removeWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeWarningListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</span></div>
<div className="block"><p>Unregisters a previously added warning listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warningListener</code> - <p>The listener instance that should no longer receive warning notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWarningsRegistry()">
<h3>getWarningsRegistry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-warningsregistry" title="class in com.here.sdk.warner">WarningsRegistry</a></span> <span className="element-name">getWarningsRegistry</span>()</div>
<div className="block"><p>Returns the centralized access point for retrieving full metadata of any supported
 warning category (e.g., safety cameras, truck restrictions, etc.).
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warningsregistry" title="class in com.here.sdk.warner"><code>WarningsRegistry</code></a> class exposes getter methods, each returning the detailed warning object for the given identifier.
 Use this getter to look up complete warning information by its id, as provided through <code>WarningListener.onWarning</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The centralized <a href="sdk-for-android-navigate-com-here-sdk-warner-warningsregistry" title="class in com.here.sdk.warner"><code>WarningsRegistry</code></a> instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">
<h3>getWarningNotificationDistances</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span className="element-name">getWarningNotificationDistances</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span></div>
<div className="block"><p>Returns the warning notification distances for the requested warning type.
 <strong>Note</strong>: <a href="sdk-for-android-navigate-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a> is not a valid value for this method.
 Use <a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine#getCustomWarningNotificationDistances(int)"><code>getCustomWarningNotificationDistances(int)</code></a> to retrieve distances for a specific
 custom warning type.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the notification distances will be returned.
     Must not be <a href="sdk-for-android-navigate-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a>.</p></dd>
<dt>Returns:</dt>
<dd><p>The warning notification distances for the given <code>warningType</code>.
     If <code>warningType</code> is <a href="sdk-for-android-navigate-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a>, a default
     <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation"><code>WarningNotificationDistances</code></a> value is returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">
<h3>setWarningNotificationDistances</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">setWarningNotificationDistances</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span></div>
<div className="block"><p>Sets the warning notification distances for the specified warning type.
 <strong>Note</strong>: <a href="sdk-for-android-navigate-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a> is not a valid value for this method.
 Use <a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine#setCustomWarningNotificationDistances(int,com.here.sdk.navigation.WarningNotificationDistances)"><code>setCustomWarningNotificationDistances(int, com.here.sdk.navigation.WarningNotificationDistances)</code></a> to configure distances for a specific
 custom warning type.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the warning notification distances will be set.
     Must not be <a href="sdk-for-android-navigate-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a>.</p></dd>
<dd><code>warningNotificationDistances</code> - <p>The warning notification distances to be set for the specified warning type.</p></dd>
<dt>Returns:</dt>
<dd><p>True if the distances were successfully set; false if <code>warningType</code> is
     <a href="sdk-for-android-navigate-warningtype#CUSTOM"><code>WarningType.CUSTOM</code></a> or the options could not be applied.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCustomWarningNotificationDistances(int)">
<h3>getCustomWarningNotificationDistances</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span className="element-name">getCustomWarningNotificationDistances</span><wbr/><span className="parameters">(int customWarningType)</span></div>
<div className="block"><p>Returns the warning notification distances for the specified custom warning type.
 Unlike <a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine#getWarningNotificationDistances(com.here.sdk.navigation.WarningType)"><code>getWarningNotificationDistances(com.here.sdk.navigation.WarningType)</code></a>, which operates on a <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation"><code>WarningType</code></a>,
 this method targets a specific custom warning category identified by <code>customWarningType</code>,
 as defined in <a href="sdk-for-android-navigate-customwarning#customWarningType"><code>CustomWarning.customWarningType</code></a> and <a href="sdk-for-android-navigate-warning#customWarningType"><code>Warning.customWarningType</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>customWarningType</code> - <p>The identifier of the custom warning type for which the
     notification distances are requested.</p></dd>
<dt>Returns:</dt>
<dd><p>The warning notification distances configured for the given <code>customWarningType</code>.
     If no distances have been explicitly set for this type, a default
     <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation"><code>WarningNotificationDistances</code></a> value is returned.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCustomWarningNotificationDistances(int,com.here.sdk.navigation.WarningNotificationDistances)">
<h3>setCustomWarningNotificationDistances</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">setCustomWarningNotificationDistances</span><wbr/><span className="parameters">(int customWarningType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span></div>
<div className="block"><p>Sets the warning notification distances for the specified custom warning type.
 Unlike <a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)"><code>setWarningNotificationDistances(com.here.sdk.navigation.WarningType, com.here.sdk.navigation.WarningNotificationDistances)</code></a>, which applies settings to a <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation"><code>WarningType</code></a>,
 this method allows configuring notification distances independently for each custom warning
 category identified by <code>customWarningType</code>, as defined in
 <a href="sdk-for-android-navigate-customwarning#customWarningType"><code>CustomWarning.customWarningType</code></a> and <a href="sdk-for-android-navigate-warning#customWarningType"><code>Warning.customWarningType</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>customWarningType</code> - <p>The identifier of the custom warning type for which the
     notification distances should be set.</p></dd>
<dd><code>warningNotificationDistances</code> - <p>The warning notification distances to be applied
     for the specified <code>customWarningType</code>.</p></dd>
<dt>Returns:</dt>
<dd><p>True if the distances were successfully set; false otherwise.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="finalizeGivenWarnings()">
<h3>finalizeGivenWarnings</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">finalizeGivenWarnings</span>()</div>
<div className="block"><p>Marks all currently active warnings as passed (<code>DistanceType.PASSED</code>), notifies all
 registered <a href="sdk-for-android-navigate-com-here-sdk-warner-warninglistener" title="interface in com.here.sdk.warner"><code>WarningListener</code></a> instances on the main thread, and then clears these
 warnings from their corresponding registries by invoking the appropriate<code>WarningsRegistry.clear<type></type></code> methods.
 This method triggers notifications only for enabled warners. Warning processing may
 occur asynchronously unless synchronous mode is enabled.
 <strong>Note</strong>: Although each warning type can also be cleared manually via the respective
 <code>WarningsRegistry.clear<type>()</type></code> methods, <code>finalizeGivenWarnings()</code> provides a
 unified way to flush all active warnings after they have been reported as
 passed. If this method is not invoked, warnings will continue to accumulate in the
 registry according to the configured warning-generation options.</p></div>
</section>
</li>
<li>
<section className="detail" id="addCustomWarningProvider(com.here.sdk.warner.CustomWarningProvider,com.here.sdk.mapdata.SegmentDataLoaderOptions)">
<h3>addCustomWarningProvider</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addCustomWarningProvider</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> segmentDataLoaderOptions)</span></div>
<div className="block"><p>Registers a custom warning provider.
 The registered provider participates in warning evaluation and is invoked
 to generate custom warnings based on the current vehicle position.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>customWarningProvider</code> - <p>A provider responsible for generating custom warnings.</p></dd>
<dd><code>segmentDataLoaderOptions</code> - <p>Specifies which data should be loaded by the <code>SegmentDataLoader</code>.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeCustomWarningProvider(com.here.sdk.warner.CustomWarningProvider)">
<h3>removeCustomWarningProvider</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeCustomWarningProvider</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider)</span></div>
<div className="block"><p>Unregisters a custom warning provider.
 After removal, the provider will no longer participate in warning evaluation
 and will not generate custom warnings.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>customWarningProvider</code> - <p>The provider to be removed.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="clearCustomWarningProviders()">
<h3>clearCustomWarningProviders</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">clearCustomWarningProviders</span>()</div>
<div className="block"><p>Unregisters all custom warning providers.
 After this call, no custom warning providers will participate in warning
 evaluation until new providers are registered.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="getWarningOptions()">
<h3>getWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a></span> <span className="element-name">getWarningOptions</span>()</div>
<div className="block"><p>Gets the currently configured <a href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions" title="class in com.here.sdk.warner"><code>WarningOptions</code></a>.
 Provides configuration parameters for all the warners.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Options that define warning behavior for all the warners.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setWarningOptions(com.here.sdk.warner.WarningOptions)">
<h3>setWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a> value)</span></div>
<div className="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions" title="class in com.here.sdk.warner"><code>WarningOptions</code></a> and updates the configuration for all the warners.
 Provides configuration parameters for all the warners.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options that define warning behavior for all the warners.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTimingProfile()">
<h3>getTimingProfile</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a></span> <span className="element-name">getTimingProfile</span>()</div>
<div className="block"><p>Gets the currently configured <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a>.
 Configures the base notification thresholds used for delivering
 navigation warnings. The effective thresholds depend on the selected
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a> and may adjust automatically according to
 the current speed limit:
 <ul>
<li>For <a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a>, thresholds apply when the current
 speed limit is above 100 km/h (62 mph).</li>
<li>For <a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a>, thresholds apply when the current
 speed limit is above 60 km/h (37 mph).</li>
<li>For <a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a>, thresholds apply when the current
 speed limit is 60 km/h (37 mph) or below.</li>
</ul>
<strong>Note:</strong> Custom threshold values can be set, but these timing-profile rules will still apply.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The timing profile that defines when navigation warnings should be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTimingProfile(com.here.sdk.navigation.TimingProfile)">
<h3>setTimingProfile</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTimingProfile</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> value)</span></div>
<div className="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a> of the current position.
 Configures the base notification thresholds used for delivering
 navigation warnings. The effective thresholds depend on the selected
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a> and may adjust automatically according to
 the current speed limit:
 <ul>
<li>For <a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a>, thresholds apply when the current
 speed limit is above 100 km/h (62 mph).</li>
<li>For <a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a>, thresholds apply when the current
 speed limit is above 60 km/h (37 mph).</li>
<li>For <a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a>, thresholds apply when the current
 speed limit is 60 km/h (37 mph) or below.</li>
</ul>
<strong>Note:</strong> Custom threshold values can be set, but these timing-profile rules will still apply.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The timing profile that defines when navigation warnings should be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">
<h3>onElectronicHorizonUpdated</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onElectronicHorizonUpdated</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</span></div>
<div className="block"><p>Called whenever the electronic horizon subsystem produces:
 <ul>
<li>a new update,</li>
<li>an error,</li>
</ul>
The client must inspect <code>error_code</code> to determine whether the call
 represents an error or a valid update.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-electronichorizonlistener#onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">onElectronicHorizonUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>errorCode</code> - <p>The error associated with the horizon computation.
     <code>null</code> means no error.</p></dd>
<dd><code>update</code> - <p>The update describing the current electronic horizon state.
     May be <code>null</code> if an update could not be produced.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
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
