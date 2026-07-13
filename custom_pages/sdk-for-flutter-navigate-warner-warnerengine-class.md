---
title: "WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/WarnerEngine-class-sidebar.html">

<div>

# <span class="kind-class">WarnerEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides the core functionality for generating and managing navigation warnings.

`WarnerEngine` processes Electronic Horizon data and determines when various types of warnings should be issued. It is used with <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a>, which supply the road topology and positional updates required for warning evaluation.

The engine monitors enabled warning types and notifies registered listeners when new warnings become available.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withenabledwarnings">WarnerEngine.WithEnabledWarnings</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-WithEnabledWarnings-param-enabledWarnings" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">enabledWarnings</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withengine">WarnerEngine.WithEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-WithEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-WithEngine-param-enabledWarnings" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">enabledWarnings</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-timingprofile">timingProfile</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>  
The timing profile that defines when navigation warnings should be triggered. Configures the base notification thresholds used for delivering navigation warnings. The effective thresholds depend on the selected <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> and may adjust automatically according to the current speed limit:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-warningoptions">warningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-warner-warningoptions-class">WarningOptions</a></span>  
Options that define warning behavior for all the warners. Provides configuration parameters for all the warners. Gets the currently configured <a href="sdk-for-flutter-navigate-warner-warningoptions-class">WarningOptions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-addcustomwarningprovider">addCustomWarningProvider</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addCustomWarningProvider-param-customWarningProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-class">CustomWarningProvider</a></span> <span class="parameter-name">customWarningProvider</span>, </span><span id="sdk-for-flutter-navigate-addCustomWarningProvider-param-segmentDataLoaderOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a></span> <span class="parameter-name">segmentDataLoaderOptions</span></span>) <span class="returntype parameter">→ void</span> </span>  
Registers a custom warning provider.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-addenabledwarnings">addEnabledWarnings</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addEnabledWarnings-param-warningTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">warningTypes</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds the given warning types to the set of warnings monitored by the engine.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-addwarninglistener">addWarningListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addWarningListener-param-warningListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warninglistener-class">WarningListener</a></span> <span class="parameter-name">warningListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Registers a listener that will receive warning notifications.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-clearcustomwarningproviders">clearCustomWarningProviders</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Unregisters all custom warning providers.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-finalizegivenwarnings">finalizeGivenWarnings</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Marks all currently active warnings as passed (`DistanceType.PASSED`), notifies all registered <a href="sdk-for-flutter-navigate-warner-warninglistener-class">WarningListener</a> instances on the main thread, and then clears these warnings from their corresponding registries by invoking the appropriate`WarningsRegistry.clear<Type>` methods.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances">getCustomWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getCustomWarningNotificationDistances-param-customWarningType" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">customWarningType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> </span>  
Returns the warning notification distances for the specified custom warning type.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-getenabledwarnings">getEnabledWarnings</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> </span>  
Returns the current list of enabled warning types.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances">getWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> </span>  
Returns the warning notification distances for the requested warning type.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-getwarningsregistry">getWarningsRegistry</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a></span> </span>  
Returns the centralized access point for retrieving full metadata of any supported warning category (e.g., safety cameras, truck restrictions, etc.).

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-onelectronichorizonupdated">onElectronicHorizonUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onElectronicHorizonUpdated-param-errorCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>?</span> <span class="parameter-name">errorCode</span>, </span><span id="sdk-for-flutter-navigate-onElectronicHorizonUpdated-param-update" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a>?</span> <span class="parameter-name">update</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever the electronic horizon subsystem produces:

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-removecustomwarningprovider">removeCustomWarningProvider</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeCustomWarningProvider-param-customWarningProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-class">CustomWarningProvider</a></span> <span class="parameter-name">customWarningProvider</span></span>) <span class="returntype parameter">→ void</span> </span>  
Unregisters a custom warning provider.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-removeenabledwarnings">removeEnabledWarnings</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeEnabledWarnings-param-warningTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">warningTypes</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes the given warning types from the set of warnings monitored by the engine.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-removewarninglistener">removeWarningListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeWarningListener-param-warningListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warninglistener-class">WarningListener</a></span> <span class="parameter-name">warningListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Unregisters a previously added warning listener.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances">setCustomWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setCustomWarningNotificationDistances-param-customWarningType" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">customWarningType</span>, </span><span id="sdk-for-flutter-navigate-setCustomWarningNotificationDistances-param-warningNotificationDistances" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">warningNotificationDistances</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Sets the warning notification distances for the specified custom warning type.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-setenabledwarnings">setEnabledWarnings</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setEnabledWarnings-param-warningTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">warningTypes</span></span>) <span class="returntype parameter">→ void</span> </span>  
Replaces the current set of enabled warning types with the provided list.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances">setWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span>, </span><span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningNotificationDistances" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">warningNotificationDistances</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Sets the warning notification distances for the specified warning type.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

