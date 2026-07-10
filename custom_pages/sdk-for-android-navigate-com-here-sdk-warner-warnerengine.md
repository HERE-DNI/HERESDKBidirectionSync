---
title: "WarnerEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warnerengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-warner-package-summary">com.here.sdk.warner</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.warner.WarnerEngine → com.here.NativeBase com.here.sdk.warner.WarnerEngine → com.here.sdk.warner.WarnerEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">`ElectronicHorizonListener`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">WarnerEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></span>

</div>

<div class="block">

Provides the core functionality for generating and managing navigation warnings. WarnerEngine processes Electronic Horizon data and determines when various types of warnings should be issued. It is used with ElectronicHorizonListener , which supply the road topology and positional updates required for warning evaluation. The engine monitors enabled warning types and notifies registered listeners when new warnings become available. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      WarnerEngine ( SDKNativeEngine sdkEngine, WallClock wallClock, List < WarningType > enabledWarnings)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      WarnerEngine ( SDKNativeEngine sdkEngine, List < WarningType > enabledWarnings)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      WarnerEngine ( List < WarningType > enabledWarnings)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addCustomWarningProvider ( CustomWarningProvider customWarningProvider, SegmentDataLoaderOptions segmentDataLoaderOptions)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Registers a custom warning provider.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addEnabledWarnings ( List < WarningType > warningTypes)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds the given warning types to the set of warnings monitored by the engine.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addWarningListener ( WarningListener warningListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Registers a listener that will receive warning notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      clearCustomWarningProviders ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Unregisters all custom warning providers.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      finalizeGivenWarnings ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Marks all currently active warnings as passed ( DistanceType.PASSED ), notifies all registered WarningListener instances on the main thread, and then clears these warnings from their corresponding registries by invoking the appropriate WarningsRegistry.clear\<Type\> methods.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCustomWarningNotificationDistances (int customWarningType)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the warning notification distances for the specified custom warning type.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">`WarningType`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEnabledWarnings ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the current list of enabled warning types.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">`TimingProfile`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTimingProfile ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently configured TimingProfile .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWarningNotificationDistances ( WarningType warningType)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the warning notification distances for the requested warning type.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions" title="class in com.here.sdk.warner">`WarningOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWarningOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently configured WarningOptions .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-warner-warningsregistry" title="class in com.here.sdk.warner">`WarningsRegistry`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWarningsRegistry ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the centralized access point for retrieving full metadata of any supported warning category (e.g., safety cameras, truck restrictions, etc.).

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onElectronicHorizonUpdated ( ElectronicHorizonErrorCode errorCode, ElectronicHorizonUpdate update)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Called whenever the electronic horizon subsystem produces: a new update, an error,

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeCustomWarningProvider ( CustomWarningProvider customWarningProvider)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Unregisters a custom warning provider.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeEnabledWarnings ( List < WarningType > warningTypes)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes the given warning types from the set of warnings monitored by the engine.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeWarningListener ( WarningListener warningListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Unregisters a previously added warning listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomWarningNotificationDistances (int customWarningType, WarningNotificationDistances warningNotificationDistances)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the warning notification distances for the specified custom warning type.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setEnabledWarnings ( List < WarningType > warningTypes)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Replaces the current set of enabled warning types with the provided list.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTimingProfile ( TimingProfile value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the TimingProfile of the current position.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setWarningNotificationDistances ( WarningType warningType, WarningNotificationDistances warningNotificationDistances)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the warning notification distances for the specified warning type.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setWarningOptions ( WarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the WarningOptions and updates the configuration for all the warners.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-util-List" class="section detail">

    ### WarnerEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">WarnerEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>\> enabledWarnings)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `enabledWarnings` -

    The list of warning types that should be monitored and processed by the engine. Only warnings of these types will be generated.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-java-util-List" class="section detail">

    ### WarnerEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">WarnerEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>\> enabledWarnings)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    A `SDKEngine` instance.

    `enabledWarnings` -

    The list of warning types that should be monitored and processed by the engine. Only warnings of these types will be generated.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-navigation-WallClock-java-util-List" class="section detail">

    ### WarnerEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">WarnerEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-wallclock" title="interface in com.here.sdk.navigation">WallClock</a> wallClock, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>\> enabledWarnings)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    A `SDKEngine` instance.

    `wallClock` -

    A `WallClock` instance.

    `enabledWarnings` -

    The list of warning types that should be monitored and processed by the engine. Only warnings of these types will be generated.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-addEnabledWarnings-java-util-List" class="section detail">

    ### addEnabledWarnings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addEnabledWarnings</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>\> warningTypes)</span>

    </div>

    <div class="block">

    Adds the given warning types to the set of warnings monitored by the engine. After this call, the engine will begin generating warnings for all types included in warningTypes , in addition to those that are already enabled.

    </div>

    Parameters:  
    `warningTypes` -

    Warning types to be added to the engine's active monitoring set.

    </div>

  - <div id="sdk-for-android-navigate-removeEnabledWarnings-java-util-List" class="section detail">

    ### removeEnabledWarnings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeEnabledWarnings</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>\> warningTypes)</span>

    </div>

    <div class="block">

    Removes the given warning types from the set of warnings monitored by the engine. After this call, the engine will stop generating warnings for all types included in warningTypes , while other enabled types remain unaffected.

    </div>

    Parameters:  
    `warningTypes` -

    Warning types to be removed from the engine's active monitoring set.

    </div>

  - <div id="sdk-for-android-navigate-setEnabledWarnings-java-util-List" class="section detail">

    ### setEnabledWarnings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnabledWarnings</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>\> warningTypes)</span>

    </div>

    <div class="block">

    Replaces the current set of enabled warning types with the provided list. After this call, the engine will monitor and generate warnings only for types included in warningTypes .

    </div>

    Parameters:  
    `warningTypes` -

    The complete new set of warning types the engine should track.

    </div>

  - <div id="sdk-for-android-navigate-getEnabledWarnings" class="section detail">

    ### getEnabledWarnings

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a>\></span> <span class="element-name">getEnabledWarnings</span>()

    </div>

    <div class="block">

    Returns the current list of enabled warning types. If the WarnerEngine was retrieved from the Navigator , it will also contain all the warnings enabled for which listeners are set.

    </div>

    Returns:  
    The currect list instance.

    </div>

  - <div id="sdk-for-android-navigate-addWarningListener-com-here-sdk-warner-WarningListener" class="section detail">

    ### addWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addWarningListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</span>

    </div>

    <div class="block">

    Registers a listener that will receive warning notifications.

    </div>

    Parameters:  
    `warningListener` -

    The listener instance that should be notified when new warnings are generated.

    </div>

  - <div id="sdk-for-android-navigate-removeWarningListener-com-here-sdk-warner-WarningListener" class="section detail">

    ### removeWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeWarningListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warninglistener" title="interface in com.here.sdk.warner">WarningListener</a> warningListener)</span>

    </div>

    <div class="block">

    Unregisters a previously added warning listener.

    </div>

    Parameters:  
    `warningListener` -

    The listener instance that should no longer receive warning notifications.

    </div>

  - <div id="sdk-for-android-navigate-getWarningsRegistry" class="section detail">

    ### getWarningsRegistry

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-warningsregistry" title="class in com.here.sdk.warner">WarningsRegistry</a></span> <span class="element-name">getWarningsRegistry</span>()

    </div>

    <div class="block">

    Returns the centralized access point for retrieving full metadata of any supported warning category (e.g., safety cameras, truck restrictions, etc.). WarningsRegistry class exposes getter methods, each returning the detailed warning object for the given identifier. Use this getter to look up complete warning information by its id, as provided through WarningListener.onWarning .

    </div>

    Returns:  
    The centralized <a href="sdk-for-android-navigate-com-here-sdk-warner-warningsregistry" title="class in com.here.sdk.warner">`WarningsRegistry`</a> instance.

    </div>

  - <div id="sdk-for-android-navigate-getWarningNotificationDistances-com-here-sdk-navigation-WarningType" class="section detail">

    ### getWarningNotificationDistances

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getWarningNotificationDistances</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span>

    </div>

    <div class="block">

    Returns the warning notification distances for the requested warning type. Note : WarningType.CUSTOM is not a valid value for this method. Use getCustomWarningNotificationDistances(int) to retrieve distances for a specific custom warning type.

    </div>

    Parameters:  
    `warningType` -

    The warning type for which the notification distances will be returned. Must not be <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype#CUSTOM">`WarningType.CUSTOM`</a>.

    Returns:  
    The warning notification distances for the given `warningType`. If `warningType` is <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype#CUSTOM">`WarningType.CUSTOM`</a>, a default <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a> value is returned.

    </div>

  - <div id="sdk-for-android-navigate-setWarningNotificationDistances-com-here-sdk-navigation-WarningType-com-here-sdk-navigation-WarningNotificationDistances" class="section detail">

    ### setWarningNotificationDistances

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setWarningNotificationDistances</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span>

    </div>

    <div class="block">

    Sets the warning notification distances for the specified warning type. Note : WarningType.CUSTOM is not a valid value for this method. Use setCustomWarningNotificationDistances(int, com.here.sdk.navigation.WarningNotificationDistances) to configure distances for a specific custom warning type.

    </div>

    Parameters:  
    `warningType` -

    The warning type for which the warning notification distances will be set. Must not be <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype#CUSTOM">`WarningType.CUSTOM`</a>.

    `warningNotificationDistances` -

    The warning notification distances to be set for the specified warning type.

    Returns:  
    True if the distances were successfully set; false if `warningType` is <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype#CUSTOM">`WarningType.CUSTOM`</a> or the options could not be applied.

    </div>

  - <div id="sdk-for-android-navigate-getCustomWarningNotificationDistances-int" class="section detail">

    ### getCustomWarningNotificationDistances

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getCustomWarningNotificationDistances</span><wbr></wbr><span class="parameters">(int customWarningType)</span>

    </div>

    <div class="block">

    Returns the warning notification distances for the specified custom warning type. Unlike getWarningNotificationDistances(com.here.sdk.navigation.WarningType) , which operates on a WarningType , this method targets a specific custom warning category identified by customWarningType , as defined in CustomWarning.customWarningType and Warning.customWarningType .

    </div>

    Parameters:  
    `customWarningType` -

    The identifier of the custom warning type for which the notification distances are requested.

    Returns:  
    The warning notification distances configured for the given `customWarningType`. If no distances have been explicitly set for this type, a default <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a> value is returned. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  - <div id="sdk-for-android-navigate-setCustomWarningNotificationDistances-int-com-here-sdk-navigation-WarningNotificationDistances" class="section detail">

    ### setCustomWarningNotificationDistances

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setCustomWarningNotificationDistances</span><wbr></wbr><span class="parameters">(int customWarningType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span>

    </div>

    <div class="block">

    Sets the warning notification distances for the specified custom warning type. Unlike setWarningNotificationDistances(com.here.sdk.navigation.WarningType, com.here.sdk.navigation.WarningNotificationDistances) , which applies settings to a WarningType , this method allows configuring notification distances independently for each custom warning category identified by customWarningType , as defined in CustomWarning.customWarningType and Warning.customWarningType .

    </div>

    Parameters:  
    `customWarningType` -

    The identifier of the custom warning type for which the notification distances should be set.

    `warningNotificationDistances` -

    The warning notification distances to be applied for the specified `customWarningType`.

    Returns:  
    True if the distances were successfully set; false otherwise. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  - <div id="sdk-for-android-navigate-finalizeGivenWarnings" class="section detail">

    ### finalizeGivenWarnings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">finalizeGivenWarnings</span>()

    </div>

    <div class="block">

    Marks all currently active warnings as passed ( DistanceType.PASSED ), notifies all registered WarningListener instances on the main thread, and then clears these warnings from their corresponding registries by invoking the appropriate WarningsRegistry.clear\<Type\> methods. This method triggers notifications only for enabled warners. Warning processing may occur asynchronously unless synchronous mode is enabled. Note : Although each warning type can also be cleared manually via the respective WarningsRegistry.clear\<Type\>() methods, finalizeGivenWarnings() provides a unified way to flush all active warnings after they have been reported as passed. If this method is not invoked, warnings will continue to accumulate in the registry according to the configured warning-generation options.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-addCustomWarningProvider-com-here-sdk-warner-CustomWarningProvider-com-here-sdk-mapdata-SegmentDataLoaderOptions" class="section detail">

    ### addCustomWarningProvider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCustomWarningProvider</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> segmentDataLoaderOptions)</span>

    </div>

    <div class="block">

    Registers a custom warning provider. The registered provider participates in warning evaluation and is invoked to generate custom warnings based on the current vehicle position.

    </div>

    Parameters:  
    `customWarningProvider` -

    A provider responsible for generating custom warnings.

    `segmentDataLoaderOptions` -

    Specifies which data should be loaded by the `SegmentDataLoader`. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  - <div id="sdk-for-android-navigate-removeCustomWarningProvider-com-here-sdk-warner-CustomWarningProvider" class="section detail">

    ### removeCustomWarningProvider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCustomWarningProvider</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-customwarningprovider" title="interface in com.here.sdk.warner">CustomWarningProvider</a> customWarningProvider)</span>

    </div>

    <div class="block">

    Unregisters a custom warning provider. After removal, the provider will no longer participate in warning evaluation and will not generate custom warnings.

    </div>

    Parameters:  
    `customWarningProvider` -

    The provider to be removed. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  - <div id="sdk-for-android-navigate-clearCustomWarningProviders" class="section detail">

    ### clearCustomWarningProviders

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCustomWarningProviders</span>()

    </div>

    <div class="block">

    Unregisters all custom warning providers. After this call, no custom warning providers will participate in warning evaluation until new providers are registered. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-getWarningOptions" class="section detail">

    ### getWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a></span> <span class="element-name">getWarningOptions</span>()

    </div>

    <div class="block">

    Gets the currently configured WarningOptions . Provides configuration parameters for all the warners.

    </div>

    Returns:  
    Options that define warning behavior for all the warners.

    </div>

  - <div id="sdk-for-android-navigate-setWarningOptions-com-here-sdk-warner-WarningOptions" class="section detail">

    ### setWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions" title="class in com.here.sdk.warner">WarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets the WarningOptions and updates the configuration for all the warners. Provides configuration parameters for all the warners.

    </div>

    Parameters:  
    `value` -

    Options that define warning behavior for all the warners.

    </div>

  - <div id="sdk-for-android-navigate-getTimingProfile" class="section detail">

    ### getTimingProfile

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a></span> <span class="element-name">getTimingProfile</span>()

    </div>

    <div class="block">

    Gets the currently configured TimingProfile . Configures the base notification thresholds used for delivering navigation warnings. The effective thresholds depend on the selected TimingProfile and may adjust automatically according to the current speed limit: For TimingProfile.FAST_SPEED , thresholds apply when the current speed limit is above 100 km/h (62 mph). For TimingProfile.REGULAR_SPEED , thresholds apply when the current speed limit is above 60 km/h (37 mph). For TimingProfile.SLOW_SPEED , thresholds apply when the current speed limit is 60 km/h (37 mph) or below. Note: Custom threshold values can be set, but these timing-profile rules will still apply.

    </div>

    Returns:  
    The timing profile that defines when navigation warnings should be triggered.

    </div>

  - <div id="sdk-for-android-navigate-setTimingProfile-com-here-sdk-navigation-TimingProfile" class="section detail">

    ### setTimingProfile

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTimingProfile</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> value)</span>

    </div>

    <div class="block">

    Sets the TimingProfile of the current position. Configures the base notification thresholds used for delivering navigation warnings. The effective thresholds depend on the selected TimingProfile and may adjust automatically according to the current speed limit: For TimingProfile.FAST_SPEED , thresholds apply when the current speed limit is above 100 km/h (62 mph). For TimingProfile.REGULAR_SPEED , thresholds apply when the current speed limit is above 60 km/h (37 mph). For TimingProfile.SLOW_SPEED , thresholds apply when the current speed limit is 60 km/h (37 mph) or below. Note: Custom threshold values can be set, but these timing-profile rules will still apply.

    </div>

    Parameters:  
    `value` -

    The timing profile that defines when navigation warnings should be triggered.

    </div>

  - <div id="sdk-for-android-navigate-onElectronicHorizonUpdated-com-here-sdk-electronichorizon-ElectronicHorizonErrorCode-com-here-sdk-electronichorizon-ElectronicHorizonUpdate" class="section detail">

    ### onElectronicHorizonUpdated

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onElectronicHorizonUpdated</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</span>

    </div>

    <div class="block">

    Called whenever the electronic horizon subsystem produces: a new update, an error, The client must inspect error_code to determine whether the call represents an error or a valid update.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener#onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate">`onElectronicHorizonUpdated`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">`ElectronicHorizonListener`</a>

    Parameters:  
    `errorCode` -

    The error associated with the horizon computation. `null` means no error.

    `update` -

    The update describing the current electronic horizon state. May be `null` if an update could not be produced. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

