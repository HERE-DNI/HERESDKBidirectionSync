---
title: "SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/SDKNativeEngine-class-sidebar.html">

<div>

# <span class="kind-class">SDKNativeEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Holds internal services and configurations needed by various HERE SDK modules.

You can initialize the HERE SDK in two ways:

- Create a shared instance of the `SDKNativeEngine` with

      SDKNativeEngine.makeSharedInstance()

  .

- Create individual instances of the `SDKNativeEngine` via

      SDKNativeEngine()

  . Note that this does not automatically set a shared instance.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-sdknativeengine">SDKNativeEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a></span> <span class="parameter-name">options</span></span>)</span>  
Makes a new instance of SDKNativeEngine using supplied options.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-isofflinemode">isOfflineMode</a></span> <span class="signature">↔ bool</span>  
The offline mode. Sets offline mode for the HERE SDK to offline or online. Defaults to false, which means the HERE SDK uses an online connection. When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set. See <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-passthroughfeatures">SDKNativeEngine.passThroughFeatures</a>. Note that the flag does not cancel pending requests. The mode can be enabled or disabled at any time. In order to fully operate offline, the mode needs to be enabled via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-offlinemode">SDKOptions.offlineMode</a>. Initialization of the HERE SDK itself does not require an internet connection. Returns `true` if the HERE SDK uses offline connection mode, otherwise returns `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-options">options</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a></span>  
Options used by this instance of <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>. Gets the options used by this instance of <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-passthroughfeatures">passThroughFeatures</a></span> <span class="signature">↔ Set<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-passthroughfeature">PassThroughFeature</a></span>\></span>?</span>  
The pass through features. Sets pass through features which are allowed to use online data when HERE SDK is in offline mode. Pass through features can be updated at any time. When offline mode is disabled, existing pass through features will be removed. These needs to be set again when you enable offline mode next time. By default, reporting of HERE SDK <a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> will be enabled when at least one pass-through feature is set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-proxysettings">proxySettings</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-proxysettings-class">ProxySettings</a>?</span>  
Proxy settings of this SDK engine that will be used by HERE SDK network for all requests. Defaults to (`null`), which indicates proxy is not enabled. When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings. Pass (`null`) to indicate that proxy should be disabled. If proxy is necessary from the start then it's recommended to use <a href="sdk-for-flutter-navigate-core-engine-networksettings-proxysettings">NetworkSettings.proxySettings</a> in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-networksettings">SDKOptions.networkSettings</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-sdkusagestats">sdkUsageStats</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a></span>\></span></span>  
Gets a list of usage statistics for all available HERE SDK features. <a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> has cache and persistent storage. Reads from the persistent storage happen on `SDKNativeEngine` creation step. Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-clearpersistentusagestats">clearPersistentUsageStats</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Clear persistent storage for the HERE SDK <a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a>.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-clearusagestatscache">clearUsageStatsCache</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Clear cache for the HERE SDK <a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a>.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-dispose">dispose</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ Future<span class="signature">\<<wbr></wbr><span class="type-parameter">void</span>\></span></span> </span>  
Stops pending requests and closes open files and databases in main thread.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-enableusagestats">enableUsageStats</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-enableUsageStats-param-enabled" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enabled</span></span>) <span class="returntype parameter">→ void</span> </span>  
Enable or disable <a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> for the HERE SDK.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-getdeviceid">getDeviceId</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ Future<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> </span>  
The unique identifier assigned to the device for this application.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-purgememorycaches">purgeMemoryCaches</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-purgeMemoryCaches-param-strategy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeenginepurgememorystrategy">SDKNativeEnginePurgeMemoryStrategy</a></span> <span class="parameter-name">strategy</span></span>) <span class="returntype parameter">→ void</span> </span>  
Releases memory occupied by internal caches.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-setaccesskeysecret">setAccessKeySecret</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setAccessKeySecret-param-accessKeySecret" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">accessKeySecret</span></span>) <span class="returntype parameter">→ void</span> </span>  
Overrides HERE SDK access key secret with new value.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-setaccessscope">setAccessScope</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setAccessScope-param-scope" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">scope</span></span>) <span class="returntype parameter">→ void</span> </span>  
Overrides the token scope of the HERE SDK with new value.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-parameterconfig">parameterConfig</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-parameterconfiguration-class">ParameterConfiguration</a></span>  
Configuration for default values of parameters used in the HERE SDK. **Note:** This feature is in beta state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. Gets the configuration for default values of parameters used in the HERE SDK.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-sharedinstance">sharedInstance</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>?</span>  
Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine. This is automatically set as a part of the SDK initialization process. Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-makesharedinstance">makeSharedInstance</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-makeSharedInstance-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a></span> <span class="parameter-name">options</span></span>) <span class="returntype parameter">→ Future<span class="signature">\<<wbr></wbr><span class="type-parameter">void</span>\></span></span> </span>  
Makes a new instance of SDKNativeEngine using supplied options and stores it as shared instance see <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-sharedinstance">SDKNativeEngine.sharedInstance</a>.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

