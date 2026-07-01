---
title: "SDKNativeEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.core.engine.SDKNativeEngine →
com.here.NativeBase → com.here.sdk.core.engine.SDKNativeEngine

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">SDKNativeEngine</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Holds internal services and configurations needed by various HERE SDK
modules. You can initialize the HERE SDK in two ways: Create a shared
instance of the SDKNativeEngine with
SDKNativeEngine.makeSharedInstance() . Create individual instances of
the SDKNativeEngine via SDKNativeEngine() . Note that this does not
automatically set a shared instance.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine-purgememorystrategy"
  class="type-name-link"
  title="enum class in com.here.sdk.core.engine"><code>SDKNativeEngine.PurgeMemoryStrategy</code></a></td>
  <td><div class="block">
  Enum representing a strategy to flush memory caches.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>SDKNativeEngine(android.content.Context androidContext,
   SDKOptions options)</code></pre></td>
  <td><div class="block">
  Makes a new instance of SDKNativeEngine using supplied options.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>clearPersistentUsageStats()</code></pre></td>
  <td><div class="block">
  Clear persistent storage for the HERE SDK UsageStats .
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>clearUsageStatsCache()</code></pre></td>
  <td><div class="block">
  Clear cache for the HERE SDK UsageStats .
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>dispose()</code></pre></td>
  <td><div class="block">
  Stops pending requests and closes open files and databases .
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>enableUsageStats(boolean enabled)</code></pre></td>
  <td><div class="block">
  Enable or disable UsageStats for the HERE SDK.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>getDeviceId(DeviceIdCallback callback)</code></pre></td>
  <td><div class="block">
  The unique identifier assigned to the device for this application.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions"
  title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a></td>
  <td><pre><code>getOptions()</code></pre></td>
  <td><div class="block">
  Gets the options used by this instance of SDKNativeEngine .
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-parameterconfiguration"
  title="class in com.here.sdk.core"><code>ParameterConfiguration</code></a></td>
  <td><pre><code>getParameterConfig()</code></pre></td>
  <td><div class="block">
  Gets the configuration for default values of parameters used in the HERE
  SDK.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html"
  class="external-link"
  title="class or interface in java.util"><code>Set</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-passthroughfeature"
  title="enum class in com.here.sdk.core.engine"><code>PassThroughFeature</code></a><code>&gt;</code></td>
  <td><pre><code>getPassThroughFeatures()</code></pre></td>
  <td><div class="block">
  Gets the pass through features.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings"
  title="class in com.here.sdk.core.engine"><code>ProxySettings</code></a></td>
  <td><pre><code>getProxySettings()</code></pre></td>
  <td><div class="block">
  Gets the current proxy settings.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats"
  title="class in com.here.sdk.core.engine"><code>UsageStats</code></a><code>&gt;</code></td>
  <td><pre><code>getSdkUsageStats()</code></pre></td>
  <td><div class="block">
  Gets a list of usage statistics for all available HERE SDK features.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine"
  title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a></td>
  <td><pre><code>getSharedInstance()</code></pre></td>
  <td><div class="block">
  Gets the shared instance of this SDK engine that can be accessed by any
  HERE SDK module as the default engine.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isOfflineMode()</code></pre></td>
  <td><div class="block">
  Gets the current offline mode.
  </div></td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>makeSharedInstance(android.content.Context androidContext,
   SDKOptions options)</code></pre></td>
  <td><div class="block">
  Makes a new instance of this class using the supplied options and stores
  it as shared instance see getSharedInstance() .
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>purgeMemoryCaches(SDKNativeEngine.PurgeMemoryStrategy strategy)</code></pre></td>
  <td><div class="block">
  Releases memory occupied by internal caches.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setAccessKeySecret(String accessKeySecret)</code></pre></td>
  <td><div class="block">
  Overrides HERE SDK access key secret with new value.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setAccessScope(String scope)</code></pre></td>
  <td><div class="block">
  Overrides the token scope of the HERE SDK with new value.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setOfflineMode(boolean value)</code></pre></td>
  <td><div class="block">
  Sets the offline mode.
  </div></td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>setParameterConfig(ParameterConfiguration value)</code></pre></td>
  <td><div class="block">
  Sets the configuration for default values of parameters used in the HERE
  SDK.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setPassThroughFeatures(Set&lt;PassThroughFeature&gt; value)</code></pre></td>
  <td><div class="block">
  Sets the pass through features.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setProxySettings(ProxySettings value)</code></pre></td>
  <td><div class="block">
  Sets the proxy settings.
  </div></td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>setSharedInstance(SDKNativeEngine value)</code></pre></td>
  <td><div class="block">
  Sets the shared instance of this SDK engine that can be accessed by any
  HERE SDK module as the default engine.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(android.content.Context,com.here.sdk.core.engine.SDKOptions)"
    class="section detail">

    ### SDKNativeEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SDKNativeEngine</span><span class="parameters">(@NonNull
    android.content.Context androidContext, @NonNull
    [SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine") options)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Makes a new instance of SDKNativeEngine using supplied options.

    </div>

    Parameters:  
    `androidContext` -

    The Android context

    `options` -

    The options for the new engine.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="setAccessKeySecret(java.lang.String)"
    class="section detail">

    ### setAccessKeySecret

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAccessKeySecret</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> accessKeySecret)</span>

    </div>

    <div class="block">

    Overrides HERE SDK access key secret with new value. The new
    credentials will be used for new requests. Note: This method can be
    called from any thread. Access key ID can be set with constructor of
    SDKNativeEngine. New instance of SDKNativeEngine should be used if a
    new access key ID is required.

    </div>

    Parameters:  
    `accessKeySecret` -

    New access key secret.

    </div>

  - <div id="setAccessScope(java.lang.String)" class="section detail">

    ### setAccessScope

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAccessScope</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> scope)</span>

    </div>

    <div class="block">

    Overrides the token scope of the HERE SDK with new value. A new
    token will be fetched with the set scope and used for future
    requests. Setting an empty string will fetch a token for the global
    scope. This method can be called from any thread.

    </div>

    Parameters:  
    `scope` -

    New scope for token

    </div>

  - <div id="dispose()" class="section detail">

    ### dispose

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()

    </div>

    <div class="block">

    Stops pending requests and closes open files and databases . Dispose
    signal is sent to dependent modules. Usage of engine, or dependent
    modules after calling dispose leads to undefined behavior. Please be
    aware that this method does not clean any type of storage. Note:
    This method should be called from main thread.

    </div>

    </div>

  - <div id="enableUsageStats(boolean)" class="section detail">

    ### enableUsageStats

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableUsageStats</span><span class="parameters">(boolean enabled)</span>

    </div>

    <div class="block">

    Enable or disable UsageStats for the HERE SDK. Defaults to disabled
    (false). When enabled, SDKNativeEngine.getSdkUsageStats() returns
    actual online data consumption. Note that the flag does not cancel
    pending requests. UsageStats can be enabled or disabled at any time.
    Note: This is a beta release of this feature, so there could be a
    few bugs and unexpected behaviors. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Parameters:  
    `enabled` -

    True, if UsageStats are enabled.

    </div>

  - <div id="makeSharedInstance(android.content.Context,com.here.sdk.core.engine.SDKOptions)"
    class="section detail">

    ### makeSharedInstance

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">makeSharedInstance</span><span class="parameters">(@NonNull
    android.content.Context androidContext, @NonNull
    [SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine") options)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Makes a new instance of this class using the supplied options and
    stores it as shared instance see getSharedInstance() . If there was
    a previously shared instance then it's disposed (so there is no need
    to call dispose() on app side) before the new instance is created.
    Note: The HERE SDK is not guaranteed to be thread safe and it is
    required to make calls to the SDK - including this one - from the
    main thread.

    </div>

    Parameters:  
    `androidContext` -

    The Android context

    `options` -

    The options for the new engine.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="clearPersistentUsageStats()" class="section detail">

    ### clearPersistentUsageStats

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearPersistentUsageStats</span>()

    </div>

    <div class="block">

    Clear persistent storage for the HERE SDK UsageStats . Note: This is
    a beta release of this feature, so there could be a few bugs and
    unexpected behaviors. Related APIs may change for new releases
    without a deprecation process.

    </div>

    </div>

  - <div id="clearUsageStatsCache()" class="section detail">

    ### clearUsageStatsCache

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearUsageStatsCache</span>()

    </div>

    <div class="block">

    Clear cache for the HERE SDK UsageStats . Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    </div>

  - <div id="purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)"
    class="section detail">

    ### purgeMemoryCaches

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">purgeMemoryCaches</span><span class="parameters">(@NonNull
    [SDKNativeEngine.PurgeMemoryStrategy](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine-purgememorystrategy "enum class in com.here.sdk.core.engine") strategy)</span>

    </div>

    <div class="block">

    Releases memory occupied by internal caches. Purging caches reduces
    memory footprint of application and may temporary reduce
    performance.

    </div>

    Parameters:  
    `strategy` -

    Option to control how much memory caches will be purged.

    </div>

  - <div id="getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)"
    class="section detail">

    ### getDeviceId

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getDeviceId</span><span class="parameters">(@NonNull
    [DeviceIdCallback](sdk-for-android-explore-com-here-sdk-core-engine-deviceidcallback "interface in com.here.sdk.core.engine") callback)</span>

    </div>

    <div class="block">

    The unique identifier assigned to the device for this application.
    This device ID is primarily used for tracking Monthly Active Users
    (MAUs).

    </div>

    Parameters:  
    `callback` -

    Callback which receives the result on the main thread.

    </div>

  - <div id="getOptions()" class="section detail">

    ### getOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine")</span> <span class="element-name">getOptions</span>()

    </div>

    <div class="block">

    Gets the options used by this instance of SDKNativeEngine .

    </div>

    Returns:  
    Options used by this instance of
    [`SDKNativeEngine`](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine").

    </div>

  - <div id="getSharedInstance()" class="section detail">

    ### getSharedInstance

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine")</span> <span class="element-name">getSharedInstance</span>()

    </div>

    <div class="block">

    Gets the shared instance of this SDK engine that can be accessed by
    any HERE SDK module as the default engine. This is automatically set
    as a part of the SDK initialization process.

    </div>

    Returns:  
    Shared instance of this SDK engine that can be accessed by any HERE
    SDK module as the default engine.

    </div>

  - <div id="setSharedInstance(com.here.sdk.core.engine.SDKNativeEngine)"
    class="section detail">

    ### setSharedInstance

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setSharedInstance</span><span class="parameters">(@Nullable
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") value)</span>

    </div>

    <div class="block">

    Sets the shared instance of this SDK engine that can be accessed by
    any HERE SDK module as the default engine. This is automatically set
    as a part of the SDK initialization process.

    </div>

    Parameters:  
    `value` -

    Shared instance of this SDK engine that can be accessed by any HERE
    SDK module as the default engine.

    </div>

  - <div id="isOfflineMode()" class="section detail">

    ### isOfflineMode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOfflineMode</span>()

    </div>

    <div class="block">

    Gets the current offline mode. Sets offline mode for the HERE SDK to
    offline or online. Defaults to false, which means the HERE SDK uses
    an online connection. When enabled, this prevents the HERE SDK from
    initiating any online connection except for provided pass through
    features if set. See getPassThroughFeatures() . Note that the flag
    does not cancel pending requests. The mode can be enabled or
    disabled at any time. In order to fully operate offline, the mode
    needs to be enabled via SDKOptions.offlineMode . Initialization of
    the HERE SDK itself does not require an internet connection. Returns
    true if the HERE SDK uses offline connection mode, otherwise returns
    false . Note: This is a beta release of this feature, so there could
    be a few bugs and unexpected behaviors. Related APIs may change for
    new releases without a deprecation process.

    </div>

    Returns:  
    The offline mode.

    </div>

  - <div id="setOfflineMode(boolean)" class="section detail">

    ### setOfflineMode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOfflineMode</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets the offline mode. Sets offline mode for the HERE SDK to offline
    or online. Defaults to false, which means the HERE SDK uses an
    online connection. When enabled, this prevents the HERE SDK from
    initiating any online connection except for provided pass through
    features if set. See getPassThroughFeatures() . Note that the flag
    does not cancel pending requests. The mode can be enabled or
    disabled at any time. In order to fully operate offline, the mode
    needs to be enabled via SDKOptions.offlineMode . Initialization of
    the HERE SDK itself does not require an internet connection. Returns
    true if the HERE SDK uses offline connection mode, otherwise returns
    false . Note: This is a beta release of this feature, so there could
    be a few bugs and unexpected behaviors. Related APIs may change for
    new releases without a deprecation process.

    </div>

    Parameters:  
    `value` -

    The offline mode.

    </div>

  - <div id="getPassThroughFeatures()" class="section detail">

    ### getPassThroughFeatures

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html"
    class="external-link" title="class or interface in java.util">Set</a><[PassThroughFeature](sdk-for-android-explore-com-here-sdk-core-engine-passthroughfeature "enum class in com.here.sdk.core.engine")></span> <span class="element-name">getPassThroughFeatures</span>()

    </div>

    <div class="block">

    Gets the pass through features. Sets pass through features which are
    allowed to use online data when HERE SDK is in offline mode. Pass
    through features can be updated at any time. When offline mode is
    disabled, existing pass through features will be removed. These
    needs to be set again when you enable offline mode next time. By
    default, reporting of HERE SDK UsageStats will be enabled when at
    least one pass-through feature is set. Note: This is a beta release
    of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    Returns:  
    The pass through features.

    </div>

  - <div id="setPassThroughFeatures(java.util.Set)"
    class="section detail">

    ### setPassThroughFeatures

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPassThroughFeatures</span><span class="parameters">(@Nullable
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html"
    class="external-link" title="class or interface in java.util">Set</a><[PassThroughFeature](sdk-for-android-explore-com-here-sdk-core-engine-passthroughfeature "enum class in com.here.sdk.core.engine")> value)</span>

    </div>

    <div class="block">

    Sets the pass through features. Sets pass through features which are
    allowed to use online data when HERE SDK is in offline mode. Pass
    through features can be updated at any time. When offline mode is
    disabled, existing pass through features will be removed. These
    needs to be set again when you enable offline mode next time. By
    default, reporting of HERE SDK UsageStats will be enabled when at
    least one pass-through feature is set. Note: This is a beta release
    of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    Parameters:  
    `value` -

    The pass through features.

    </div>

  - <div id="getParameterConfig()" class="section detail">

    ### getParameterConfig

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[ParameterConfiguration](sdk-for-android-explore-com-here-sdk-core-parameterconfiguration "class in com.here.sdk.core")</span> <span class="element-name">getParameterConfig</span>()

    </div>

    <div class="block">

    Gets the configuration for default values of parameters used in the
    HERE SDK. Note: This feature is in beta state and thus there can be
    bugs and unexpected behavior. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Returns:  
    Configuration for default values of parameters used in the HERE SDK.

    </div>

  - <div id="setParameterConfig(com.here.sdk.core.ParameterConfiguration)"
    class="section detail">

    ### setParameterConfig

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setParameterConfig</span><span class="parameters">(@NonNull
    [ParameterConfiguration](sdk-for-android-explore-com-here-sdk-core-parameterconfiguration "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the configuration for default values of parameters used in the
    HERE SDK. Note: This feature is in beta state and thus there can be
    bugs and unexpected behavior. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Parameters:  
    `value` -

    Configuration for default values of parameters used in the HERE SDK.

    </div>

  - <div id="getProxySettings()" class="section detail">

    ### getProxySettings

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ProxySettings](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings "class in com.here.sdk.core.engine")</span> <span class="element-name">getProxySettings</span>()

    </div>

    <div class="block">

    Gets the current proxy settings. Defaults to ( null ), which
    indicates proxy is not enabled. When setting proxy settings, they
    will immediately be applied and all the pending and fresh requests
    will use these settings. Pass ( null ) to indicate that proxy should
    be disabled. If proxy is necessary from the start then it's
    recommended to use NetworkSettings.proxySettings in
    SDKOptions.networkSettings . Note: This is a beta release of this
    feature, so there could be a few bugs and unexpected behaviors.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    Returns:  
    Proxy settings of this SDK engine that will be used by HERE SDK
    network for all requests.

    </div>

  - <div id="setProxySettings(com.here.sdk.core.engine.ProxySettings)"
    class="section detail">

    ### setProxySettings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProxySettings</span><span class="parameters">(@Nullable
    [ProxySettings](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings "class in com.here.sdk.core.engine") value)</span>

    </div>

    <div class="block">

    Sets the proxy settings. Defaults to ( null ), which indicates proxy
    is not enabled. When setting proxy settings, they will immediately
    be applied and all the pending and fresh requests will use these
    settings. Pass ( null ) to indicate that proxy should be disabled.
    If proxy is necessary from the start then it's recommended to use
    NetworkSettings.proxySettings in SDKOptions.networkSettings . Note:
    This is a beta release of this feature, so there could be a few bugs
    and unexpected behaviors. Related APIs may change for new releases
    without a deprecation process.

    </div>

    Parameters:  
    `value` -

    Proxy settings of this SDK engine that will be used by HERE SDK
    network for all requests.

    </div>

  - <div id="getSdkUsageStats()" class="section detail">

    ### getSdkUsageStats

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[UsageStats](sdk-for-android-explore-com-here-sdk-core-engine-usagestats "class in com.here.sdk.core.engine")></span> <span class="element-name">getSdkUsageStats</span>()

    </div>

    <div class="block">

    Gets a list of usage statistics for all available HERE SDK features.
    UsageStats has cache and persistent storage. Reads from the
    persistent storage happen on SDKNativeEngine creation step. Writes
    to persistent storage happen by reaching internal limit (amount of
    upload bytes, by default is 50KB). Note: This is a beta release of
    this feature, so there could be a few bugs and unexpected behaviors.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    Returns:  
    Gets a list of usage statistics for all available HERE SDK features.

    </div>

  </div>

</div>

