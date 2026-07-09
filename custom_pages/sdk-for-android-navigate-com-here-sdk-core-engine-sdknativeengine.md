---
title: "SDKNativeEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SDKNativeEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.engine.SDKNativeEngine</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SDKNativeEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Holds internal services and configurations needed by various HERE SDK modules.
 You can initialize the HERE SDK in two ways:
 <ul>
<li>Create a shared instance of the <code>SDKNativeEngine</code> with <code>SDKNativeEngine.makeSharedInstance()</code>.</li>
<li>Create individual instances of the <code>SDKNativeEngine</code> via <code>SDKNativeEngine()</code>. Note that this does not automatically set a shared instance.</li>
</ul></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine-purgememorystrategy" title="enum class in com.here.sdk.core.engine">SDKNativeEngine.PurgeMemoryStrategy</a></code></div>
<div className="col-last even-row-color">
<div className="block">Enum representing a strategy to flush memory caches.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine#%3Cinit%3E(android.content.Context,com.here.sdk.core.engine.SDKOptions)">SDKNativeEngine</a><wbr/>(android.content.Context androidContext,
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</code></div>
<div className="col-last even-row-color">
<div className="block">Makes a new instance of SDKNativeEngine using supplied options.</div>
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
<section className="detail" id="&lt;init&gt;(android.content.Context,com.here.sdk.core.engine.SDKOptions)">
<h3>SDKNativeEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SDKNativeEngine</span><wbr/><span className="parameters">(@NonNull
 android.content.Context androidContext,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span>
                throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Makes a new instance of SDKNativeEngine using supplied options.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>androidContext</code> - <p>The Android context</p></dd>
<dd><code>options</code> - <p>The options for the new engine.</p></dd>
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
<section className="detail" id="setAccessKeySecret(java.lang.String)">
<h3>setAccessKeySecret</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setAccessKeySecret</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> accessKeySecret)</span></div>
<div className="block"><p>Overrides HERE SDK access key secret with new value.
 The new credentials will be used for new requests.
 <strong>Note:</strong>
 This method can be called from any thread.
 Access key ID can be set with constructor of SDKNativeEngine.
 New instance of SDKNativeEngine should be used if a new access key ID is required.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>accessKeySecret</code> - <p>New access key secret.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setAccessScope(java.lang.String)">
<h3>setAccessScope</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setAccessScope</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> scope)</span></div>
<div className="block"><p>Overrides the token scope of the HERE SDK with new value.
 A new token will be fetched with the set scope and used for future requests.
 Setting an empty string will fetch a token for the global scope.
 This method can be called from any thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>scope</code> - <p>New scope for token</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="dispose()">
<h3>dispose</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">dispose</span>()</div>
<div className="block"><p>Stops pending requests and closes open files and databases .
 Dispose signal is sent to dependent modules.
 Usage of engine, or dependent modules after calling dispose leads to undefined behavior.
 Please be aware that this method does not clean any type of storage.
 <strong>Note:</strong>
 This method should be called from main thread.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableUsageStats(boolean)">
<h3>enableUsageStats</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">enableUsageStats</span><wbr/><span className="parameters">(boolean enabled)</span></div>
<div className="block"><p>Enable or disable <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> for the HERE SDK. Defaults to disabled (false). When enabled, <code>SDKNativeEngine.getSdkUsageStats()</code>
 returns actual online data consumption. Note that the flag does not cancel pending requests.
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> can be enabled or disabled at any time.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>enabled</code> - <p>True, if UsageStats are enabled.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="makeSharedInstance(android.content.Context,com.here.sdk.core.engine.SDKOptions)">
<h3>makeSharedInstance</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">makeSharedInstance</span><wbr/><span className="parameters">(@NonNull
 android.content.Context androidContext,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span>
                               throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Makes a new instance of this class using the supplied options and stores it as shared instance
 see <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine#getSharedInstance()"><code>getSharedInstance()</code></a>. If there was a previously shared instance
 then it's disposed (so there is no need to call <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine#dispose()"><code>dispose()</code></a> on app side) before the new instance is created.
 <strong>Note:</strong> The HERE SDK is not guaranteed to be thread safe and it is required to make calls
 to the SDK - including this one - from the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>androidContext</code> - <p>The Android context</p></dd>
<dd><code>options</code> - <p>The options for the new engine.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="clearPersistentUsageStats()">
<h3>clearPersistentUsageStats</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">clearPersistentUsageStats</span>()</div>
<div className="block"><p>Clear persistent storage for the HERE SDK <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="clearUsageStatsCache()">
<h3>clearUsageStatsCache</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">clearUsageStatsCache</span>()</div>
<div className="block"><p>Clear cache for the HERE SDK <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)">
<h3>purgeMemoryCaches</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">purgeMemoryCaches</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine-purgememorystrategy" title="enum class in com.here.sdk.core.engine">SDKNativeEngine.PurgeMemoryStrategy</a> strategy)</span></div>
<div className="block"><p>Releases memory occupied by internal caches.
 Purging caches reduces memory footprint of application and may temporary reduce performance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>strategy</code> - <p>Option to control how much memory caches will be purged.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)">
<h3>getDeviceId</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">getDeviceId</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-deviceidcallback" title="interface in com.here.sdk.core.engine">DeviceIdCallback</a> callback)</span></div>
<div className="block"><p>The unique identifier assigned to the device for this application.
 This device ID is primarily used for tracking Monthly Active Users (MAUs).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOptions()">
<h3>getOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a></span> <span className="element-name">getOptions</span>()</div>
<div className="block"><p>Gets the options used by this instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Options used by this instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSharedInstance()">
<h3>getSharedInstance</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a></span> <span className="element-name">getSharedInstance</span>()</div>
<div className="block"><p>Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
 engine.
 This is automatically set as a part of the SDK initialization process.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
     engine.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSharedInstance(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>setSharedInstance</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setSharedInstance</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> value)</span></div>
<div className="block"><p>Sets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
 engine.
 This is automatically set as a part of the SDK initialization process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
     engine.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isOfflineMode()">
<h3>isOfflineMode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isOfflineMode</span>()</div>
<div className="block"><p>Gets the current offline mode.
 Sets offline mode for the HERE SDK to offline or online.
 Defaults to false, which means the HERE SDK uses an online connection.
 When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
 See <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine#getPassThroughFeatures()"><code>getPassThroughFeatures()</code></a>.
 Note that the flag does not cancel pending requests.
 The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
 needs to be enabled via <a href="sdk-for-android-navigate-sdkoptions#offlineMode"><code>SDKOptions.offlineMode</code></a>.
 Initialization of the HERE SDK itself does not require an internet connection.
 Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.
 Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The offline mode.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOfflineMode(boolean)">
<h3>setOfflineMode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOfflineMode</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Sets the offline mode.
 Sets offline mode for the HERE SDK to offline or online.
 Defaults to false, which means the HERE SDK uses an online connection.
 When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
 See <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine#getPassThroughFeatures()"><code>getPassThroughFeatures()</code></a>.
 Note that the flag does not cancel pending requests.
 The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
 needs to be enabled via <a href="sdk-for-android-navigate-sdkoptions#offlineMode"><code>SDKOptions.offlineMode</code></a>.
 Initialization of the HERE SDK itself does not require an internet connection.
 Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.
 Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The offline mode.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPassThroughFeatures()">
<h3>getPassThroughFeatures</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-passthroughfeature" title="enum class in com.here.sdk.core.engine">PassThroughFeature</a>&gt;</span> <span className="element-name">getPassThroughFeatures</span>()</div>
<div className="block"><p>Gets the pass through features.
 Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
 Pass through features can be updated at any time.
 When offline mode is disabled, existing pass through features will be removed.
 These needs to be set again when you enable offline mode next time.
 By default, reporting of HERE SDK <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> will be enabled when at least one pass-through feature is set.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The pass through features.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPassThroughFeatures(java.util.Set)">
<h3>setPassThroughFeatures</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPassThroughFeatures</span><wbr/><span className="parameters">(@Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-passthroughfeature" title="enum class in com.here.sdk.core.engine">PassThroughFeature</a>&gt; value)</span></div>
<div className="block"><p>Sets the pass through features.
 Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
 Pass through features can be updated at any time.
 When offline mode is disabled, existing pass through features will be removed.
 These needs to be set again when you enable offline mode next time.
 By default, reporting of HERE SDK <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> will be enabled when at least one pass-through feature is set.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The pass through features.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getParameterConfig()">
<h3>getParameterConfig</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-parameterconfiguration" title="class in com.here.sdk.core">ParameterConfiguration</a></span> <span className="element-name">getParameterConfig</span>()</div>
<div className="block"><p>Gets the configuration for default values of parameters used in the HERE SDK.
 <strong>Note:</strong> This feature is in beta state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Configuration for default values of parameters used in the HERE SDK.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setParameterConfig(com.here.sdk.core.ParameterConfiguration)">
<h3>setParameterConfig</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setParameterConfig</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-parameterconfiguration" title="class in com.here.sdk.core">ParameterConfiguration</a> value)</span></div>
<div className="block"><p>Sets the configuration for default values of parameters used in the HERE SDK.
 <strong>Note:</strong> This feature is in beta state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Configuration for default values of parameters used in the HERE SDK.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProxySettings()">
<h3>getProxySettings</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-proxysettings" title="class in com.here.sdk.core.engine">ProxySettings</a></span> <span className="element-name">getProxySettings</span>()</div>
<div className="block"><p>Gets the current proxy settings.
 Defaults to (<code>null</code>), which indicates proxy is not enabled.
 When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
 Pass (<code>null</code>) to indicate that proxy should be disabled.
 If proxy is necessary from the start then it's recommended to use <a href="sdk-for-android-navigate-networksettings#proxySettings"><code>NetworkSettings.proxySettings</code></a> in <a href="sdk-for-android-navigate-sdkoptions#networkSettings"><code>SDKOptions.networkSettings</code></a>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setProxySettings(com.here.sdk.core.engine.ProxySettings)">
<h3>setProxySettings</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setProxySettings</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-proxysettings" title="class in com.here.sdk.core.engine">ProxySettings</a> value)</span></div>
<div className="block"><p>Sets the proxy settings.
 Defaults to (<code>null</code>), which indicates proxy is not enabled.
 When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
 Pass (<code>null</code>) to indicate that proxy should be disabled.
 If proxy is necessary from the start then it's recommended to use <a href="sdk-for-android-navigate-networksettings#proxySettings"><code>NetworkSettings.proxySettings</code></a> in <a href="sdk-for-android-navigate-sdkoptions#networkSettings"><code>SDKOptions.networkSettings</code></a>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSdkUsageStats()">
<h3>getSdkUsageStats</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine">UsageStats</a>&gt;</span> <span className="element-name">getSdkUsageStats</span>()</div>
<div className="block"><p>Gets a list of usage statistics for all available HERE SDK features.
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine"><code>UsageStats</code></a> has cache and persistent storage. Reads from the persistent storage happen on <code>SDKNativeEngine</code> creation step.
 Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
