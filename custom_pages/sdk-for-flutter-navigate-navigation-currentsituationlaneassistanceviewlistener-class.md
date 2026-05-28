---
title: "CurrentSituationLaneAssistanceViewListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CurrentSituationLaneAssistanceViewListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/CurrentSituationLaneAssistanceViewListener-class.html#constructors">Constructors</a></li>
<li><a href="navigation/CurrentSituationLaneAssistanceViewListener/CurrentSituationLaneAssistanceViewListener.html">CurrentSituationLaneAssistanceViewListener</a></li>
<li class="section-title inherited">
<a href="navigation/CurrentSituationLaneAssistanceViewListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="navigation/CurrentSituationLaneAssistanceViewListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="navigation/CurrentSituationLaneAssistanceViewListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="navigation/CurrentSituationLaneAssistanceViewListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/CurrentSituationLaneAssistanceViewListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/CurrentSituationLaneAssistanceViewListener/onCurrentSituationLaneAssistanceViewUpdate.html">onCurrentSituationLaneAssistanceViewUpdate</a></li>
<li class="inherited"><a href="navigation/CurrentSituationLaneAssistanceViewListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/CurrentSituationLaneAssistanceViewListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/CurrentSituationLaneAssistanceViewListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">CurrentSituationLaneAssistanceViewListener class</li>
</ol>
<div class="self-name">CurrentSituationLaneAssistanceViewListener</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/CurrentSituationLaneAssistanceViewListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CurrentSituationLaneAssistanceViewListener class abstract</h1></div>
<section class="desc markdown">
<p>This abstract class should be
implemented in order to receive notifications on /sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class.</p>
<p>The current situation lane assistance view notifications describe the lane information at the current location.</p>
<p>A new notification is evaluated with each location update. A notification is only sent when there is a change
in lane data, such as a new upcoming lane.</p>
<p>This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode.
During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route
to reach the destination.
However, the event does not indicate which exact lane the user is currently driving in.
The listener works for offline mode as well.</p>
<p><strong>Note:</strong></p>
<ul>
<li>Lane information is not available for all roads. It's mostly available for roads with painted turn directions.</li>
<li>This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</li>
</ul>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CurrentSituationLaneAssistanceViewListener">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-currentsituationlaneassistanceviewlistener(void onCurrentSituationLaneAssistanceViewUpdateLambda(/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class))
</dt>
<dd>
          This abstract class should be
implemented in order to receive notifications on /sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onCurrentSituationLaneAssistanceViewUpdate">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-oncurrentsituationlaneassistanceviewupdate(<wbr/>/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class lanes)
    → void

</dt>
<dd>
  The callback to be called.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">CurrentSituationLaneAssistanceViewListener class</li>
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
