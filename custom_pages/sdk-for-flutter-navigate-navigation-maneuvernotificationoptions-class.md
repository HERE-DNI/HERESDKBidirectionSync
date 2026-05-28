---
title: "ManeuverNotificationOptions class"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/ManeuverNotificationOptions-class.html#constructors">Constructors</a></li>
<li><a class="deprecated" href="navigation/ManeuverNotificationOptions/ManeuverNotificationOptions.html">ManeuverNotificationOptions</a></li>
<li><a class="deprecated" href="navigation/ManeuverNotificationOptions/ManeuverNotificationOptions.withAllFields.html">withAllFields</a></li>
<li><a class="deprecated" href="navigation/ManeuverNotificationOptions/ManeuverNotificationOptions.withAllFieldsNew.html">withAllFieldsNew</a></li>
<li><a href="navigation/ManeuverNotificationOptions/ManeuverNotificationOptions.withDefaults.html">withDefaults</a></li>
<li><a class="deprecated" href="navigation/ManeuverNotificationOptions/ManeuverNotificationOptions.withTextUsageOption.html">withTextUsageOption</a></li>
<li class="section-title">
<a href="navigation/ManeuverNotificationOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/ManeuverNotificationOptions/arrivalNotificationOption.html">arrivalNotificationOption</a></li>
<li><a href="navigation/ManeuverNotificationOptions/directionInformationUsageForActionNotificationOption.html">directionInformationUsageForActionNotificationOption</a></li>
<li><a class="deprecated" href="navigation/ManeuverNotificationOptions/enableDestinationReachedNotification.html">enableDestinationReachedNotification</a></li>
<li><a href="navigation/ManeuverNotificationOptions/enableDoubleNotification.html">enableDoubleNotification</a></li>
<li><a href="navigation/ManeuverNotificationOptions/enableHighwayExit.html">enableHighwayExit</a></li>
<li><a href="navigation/ManeuverNotificationOptions/enableLaneRecommendation.html">enableLaneRecommendation</a></li>
<li><a href="navigation/ManeuverNotificationOptions/enablePhoneme.html">enablePhoneme</a></li>
<li><a href="navigation/ManeuverNotificationOptions/enableRoundaboutNotification.html">enableRoundaboutNotification</a></li>
<li><a href="navigation/ManeuverNotificationOptions/hashCode.html">hashCode</a></li>
<li><a href="navigation/ManeuverNotificationOptions/includedNaturalGuidanceTypes.html">includedNaturalGuidanceTypes</a></li>
<li><a href="navigation/ManeuverNotificationOptions/includedNotificationTypes.html">includedNotificationTypes</a></li>
<li><a href="navigation/ManeuverNotificationOptions/language.html">language</a></li>
<li><a href="navigation/ManeuverNotificationOptions/notificationFormatOption.html">notificationFormatOption</a></li>
<li class="inherited"><a href="navigation/ManeuverNotificationOptions/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/ManeuverNotificationOptions/textUsageOptions.html">textUsageOptions</a></li>
<li><a href="navigation/ManeuverNotificationOptions/unitSystem.html">unitSystem</a></li>
<li class="section-title inherited"><a href="navigation/ManeuverNotificationOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/ManeuverNotificationOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/ManeuverNotificationOptions/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/ManeuverNotificationOptions-class.html#operators">Operators</a></li>
<li><a href="navigation/ManeuverNotificationOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">ManeuverNotificationOptions class</li>
</ol>
<div class="self-name">ManeuverNotificationOptions</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ManeuverNotificationOptions class</h1></div>
<section class="desc markdown">
<p>A class containing all options to be used when generating maneuver notifications.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ManeuverNotificationOptions">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions(/sdk-for-flutter-navigate-core-languagecode language, /sdk-for-flutter-navigate-core-unitsystem unitSystem)
</dt>
<dd>
          Creates a new instance of this class with specified language and unit system.
        </dd>
<dt class="callable" id="ManeuverNotificationOptions.withAllFields">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions-withallfields(/sdk-for-flutter-navigate-core-languagecode language, /sdk-for-flutter-navigate-core-unitsystem unitSystem, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype&gt; includedNotificationTypes, bool enableRoundaboutNotification, bool enableDestinationReachedNotification, bool enableDoubleNotification, bool enablePhoneme, bool enableHighwayExit)
</dt>
<dd>
          Creates a new instance of this class with full specified configurations.
        </dd>
<dt class="callable" id="ManeuverNotificationOptions.withAllFieldsNew">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions-withallfieldsnew(/sdk-for-flutter-navigate-core-languagecode language, /sdk-for-flutter-navigate-core-unitsystem unitSystem, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype&gt; includedNotificationTypes, bool enableRoundaboutNotification, bool enableDestinationReachedNotification, bool enableDoubleNotification, bool enablePhoneme, /sdk-for-flutter-navigate-navigation-notificationformatoption notificationFormatOption, bool enableHighwayExit)
</dt>
<dd>
          Creates a new instance of this class with full specified configurations.
        </dd>
<dt class="callable" id="ManeuverNotificationOptions.withDefaults">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions-withdefaults()
</dt>
<dd>
          Creates a new instance of this class with default configurations.
        </dd>
<dt class="callable" id="ManeuverNotificationOptions.withTextUsageOption">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions-withtextusageoption(/sdk-for-flutter-navigate-core-languagecode language, /sdk-for-flutter-navigate-core-unitsystem unitSystem, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype&gt; includedNotificationTypes, bool enableRoundaboutNotification, bool enableDestinationReachedNotification, bool enableDoubleNotification, bool enablePhoneme, /sdk-for-flutter-navigate-routing-textusageoptions-class textUsageOptions, bool enableHighwayExit)
</dt>
<dd>
          Creates a new instance of this class with full specified configurations.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="arrivalNotificationOption">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-arrivalnotificationoption
↔ /sdk-for-flutter-navigate-navigation-arrivalnotificationoption
</dt>
<dd>
  A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated.
Defaults to <code>ArrivalNotificationOption.BOTH</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="directionInformationUsageForActionNotificationOption">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-directioninformationusageforactionnotificationoption
↔ /sdk-for-flutter-navigate-navigation-directioninformationusageoption
</dt>
<dd>
  An option whether direction information should be used when generating notification with
/sdk-for-flutter-navigate-navigation-maneuvernotificationtype. Defaults to /sdk-for-flutter-navigate-navigation-directioninformationusageoption.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableDestinationReachedNotification">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enabledestinationreachednotification
↔ bool
</dt>
<dd>
  A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
Defaults to <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableDoubleNotification">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enabledoublenotification
↔ bool
</dt>
<dd>
  A flag that indicates whether combined maneuver notifications should be generated.
Such double notifications can be useful when maneuvers are very close.
<strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
This way a user can better anticipate the next-next maneuver.
Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
When the next-next maneuver action takes place, the notification will be given as usual.
<strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
Defaults to <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableHighwayExit">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablehighwayexit
↔ bool
</dt>
<dd>
  A flag that indicates whether highway exit information should be used when generating notification.
Defaults to <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableLaneRecommendation">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablelanerecommendation
↔ bool
</dt>
<dd>
  A flag that indicates whether lane recommendation should be used when generating notifications.
In case the flag is enabled, <em>only</em> the notification for the /sdk-for-flutter-navigate-navigation-maneuvernotificationtype
maneuver notification type will contain the lane recommendation. The lane recommandation will replace the
direction information in the notification.
<strong>Example:</strong> 'After 250 meters use the right two lanes and turn right.'.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enablePhoneme">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablephoneme
↔ bool
</dt>
<dd>
  A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
road numbers, city names) should be used when generating notifications. Direction information comes usually
in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
direction information sound more natural.
<strong>Note:</strong> For now, this property is functional for road name and road number information only.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableRoundaboutNotification">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enableroundaboutnotification
↔ bool
</dt>
<dd>
  A flag that indicates whether notification for roundabout-related maneuvers should be generated.
Defaults to <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="includedNaturalGuidanceTypes">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-includednaturalguidancetypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-naturalguidancetype&gt;
</dt>
<dd>
  List of /sdk-for-flutter-navigate-navigation-naturalguidancetype should be included in the notifications. Excluding
all of them will disable natural guidance information in the notifications completely.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="includedNotificationTypes">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-includednotificationtypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype&gt;
</dt>
<dd>
  List of /sdk-for-flutter-navigate-navigation-maneuvernotificationtype for which notifications should be generated. Excluding all of
them will disable the maneuver notifications completely.
By default, all types are included.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="language">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-language
↔ /sdk-for-flutter-navigate-core-languagecode
</dt>
<dd>
  The language in which the notifications will be generated. When the specified language
is not supported, the default language is used, which is English (American).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="notificationFormatOption">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-notificationformatoption
↔ /sdk-for-flutter-navigate-navigation-notificationformatoption
</dt>
<dd>
  A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
and the /sdk-for-flutter-navigate-navigation-notificationformatoption orthographic form is included in the notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textUsageOptions">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-textusageoptions
↔ /sdk-for-flutter-navigate-routing-textusageoptions-class
</dt>
<dd>
  An option whether street name, road number and sign post direction should be used when generating notification.
Defaults to each attribute as /sdk-for-flutter-navigate-routing-localizedtextpreference.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="unitSystem">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-unitsystem
↔ /sdk-for-flutter-navigate-core-unitsystem
</dt>
<dd>
  Defines the measurement system used for distances. Defaults to metric.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">ManeuverNotificationOptions class</li>
</ol>
<h5>navigation library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
