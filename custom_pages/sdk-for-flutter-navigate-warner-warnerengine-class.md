---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-warnerengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarnerEngine-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">WarnerEngine class</li>
</ol>
<div class="self-name">WarnerEngine</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/WarnerEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>WarnerEngine class abstract</h1></div>
<section class="desc markdown">
<p>Provides the core functionality for generating and managing navigation warnings.</p>
<p><code>WarnerEngine</code> processes Electronic Horizon data and determines when various types
of warnings should be issued. It is used with /sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class,
which supply the road topology and positional updates required for warning evaluation.</p>
<p>The engine monitors enabled warning types and notifies registered listeners when new warnings become available.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="WarnerEngine.WithEnabledWarnings">
/sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withenabledwarnings(List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-warningtype&gt; enabledWarnings)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="WarnerEngine.WithEngine">
/sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-warningtype&gt; enabledWarnings)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timingProfile">
/sdk-for-flutter-navigate-warner-warnerengine-timingprofile
↔ /sdk-for-flutter-navigate-navigation-timingprofile
</dt>
<dd>
  The timing profile that defines when navigation warnings should be triggered.
Configures the base notification thresholds used for delivering
navigation warnings. The effective thresholds depend on the selected
/sdk-for-flutter-navigate-navigation-timingprofile and may adjust automatically according to
the current speed limit:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="warningOptions">
/sdk-for-flutter-navigate-warner-warnerengine-warningoptions
↔ /sdk-for-flutter-navigate-warner-warningoptions-class
</dt>
<dd>
  Options that define warning behavior for all the warners.
Provides configuration parameters for all the warners.
Gets the currently configured /sdk-for-flutter-navigate-warner-warningoptions-class.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addCustomWarningProvider">
/sdk-for-flutter-navigate-warner-warnerengine-addcustomwarningprovider(<wbr/>/sdk-for-flutter-navigate-warner-customwarningprovider-class customWarningProvider, /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class segmentDataLoaderOptions)
    → void

</dt>
<dd>
  Registers a custom warning provider.
  

</dd>
<dt class="callable" id="addEnabledWarnings">
/sdk-for-flutter-navigate-warner-warnerengine-addenabledwarnings(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-warningtype&gt; warningTypes)
    → void

</dt>
<dd>
  Adds the given warning types to the set of warnings monitored by the engine.
  

</dd>
<dt class="callable" id="addWarningListener">
/sdk-for-flutter-navigate-warner-warnerengine-addwarninglistener(<wbr/>/sdk-for-flutter-navigate-warner-warninglistener-class warningListener)
    → void

</dt>
<dd>
  Registers a listener that will receive warning notifications.
  

</dd>
<dt class="callable" id="clearCustomWarningProviders">
/sdk-for-flutter-navigate-warner-warnerengine-clearcustomwarningproviders(<wbr/>)
    → void

</dt>
<dd>
  Unregisters all custom warning providers.
  

</dd>
<dt class="callable" id="finalizeGivenWarnings">
/sdk-for-flutter-navigate-warner-warnerengine-finalizegivenwarnings(<wbr/>)
    → void

</dt>
<dd>
  Marks all currently active warnings as passed (<code>DistanceType.PASSED</code>), notifies all
registered /sdk-for-flutter-navigate-warner-warninglistener-class instances on the main thread, and then clears these
warnings from their corresponding registries by invoking the appropriate<code>WarningsRegistry.clear&lt;Type&gt;</code> methods.
  

</dd>
<dt class="callable" id="getCustomWarningNotificationDistances">
/sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances(<wbr/>int customWarningType)
    → /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class

</dt>
<dd>
  Returns the warning notification distances for the specified custom warning type.
  

</dd>
<dt class="callable" id="getEnabledWarnings">
/sdk-for-flutter-navigate-warner-warnerengine-getenabledwarnings(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-warningtype&gt;

</dt>
<dd>
  Returns the current list of enabled warning types.
  

</dd>
<dt class="callable" id="getWarningNotificationDistances">
/sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances(<wbr/>/sdk-for-flutter-navigate-navigation-warningtype warningType)
    → /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class

</dt>
<dd>
  Returns the warning notification distances for the requested warning type.
  

</dd>
<dt class="callable" id="getWarningsRegistry">
/sdk-for-flutter-navigate-warner-warnerengine-getwarningsregistry(<wbr/>)
    → /sdk-for-flutter-navigate-warner-warningsregistry-class

</dt>
<dd>
  Returns the centralized access point for retrieving full metadata of any supported
warning category (e.g., safety cameras, truck restrictions, etc.).
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="onElectronicHorizonUpdated">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-onelectronichorizonupdated(<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode? errorCode, /sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class? update)
    → void

</dt>
<dd class="inherited">
  Called whenever the electronic horizon subsystem produces:
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeCustomWarningProvider">
/sdk-for-flutter-navigate-warner-warnerengine-removecustomwarningprovider(<wbr/>/sdk-for-flutter-navigate-warner-customwarningprovider-class customWarningProvider)
    → void

</dt>
<dd>
  Unregisters a custom warning provider.
  

</dd>
<dt class="callable" id="removeEnabledWarnings">
/sdk-for-flutter-navigate-warner-warnerengine-removeenabledwarnings(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-warningtype&gt; warningTypes)
    → void

</dt>
<dd>
  Removes the given warning types from the set of warnings monitored by the engine.
  

</dd>
<dt class="callable" id="removeWarningListener">
/sdk-for-flutter-navigate-warner-warnerengine-removewarninglistener(<wbr/>/sdk-for-flutter-navigate-warner-warninglistener-class warningListener)
    → void

</dt>
<dd>
  Unregisters a previously added warning listener.
  

</dd>
<dt class="callable" id="setCustomWarningNotificationDistances">
/sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances(<wbr/>int customWarningType, /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class warningNotificationDistances)
    → bool

</dt>
<dd>
  Sets the warning notification distances for the specified custom warning type.
  

</dd>
<dt class="callable" id="setEnabledWarnings">
/sdk-for-flutter-navigate-warner-warnerengine-setenabledwarnings(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-warningtype&gt; warningTypes)
    → void

</dt>
<dd>
  Replaces the current set of enabled warning types with the provided list.
  

</dd>
<dt class="callable" id="setWarningNotificationDistances">
/sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances(<wbr/>/sdk-for-flutter-navigate-navigation-warningtype warningType, /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class warningNotificationDistances)
    → bool

</dt>
<dd>
  Sets the warning notification distances for the specified warning type.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">WarnerEngine class</li>
</ol>
<h5>warner library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
