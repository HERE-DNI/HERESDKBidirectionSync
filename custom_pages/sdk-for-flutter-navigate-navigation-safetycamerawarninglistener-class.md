---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SafetyCameraWarningListener-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">SafetyCameraWarningListener class</li>
</ol>
<div class="self-name">SafetyCameraWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SafetyCameraWarningListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SafetyCameraWarningListener class abstract</h1></div>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive notifications on safety cameras.</p>
<p>A <code>SafetyCameraWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>SafetyCameraWarning</code> 120 meters and <code>SafetyCameraWarning</code> 160 meters ahead,
the first <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters
and the next <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<p>When <code>SafetyCameraWarningListener</code> is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled.
The updates for the same safety camera appear in order of the initial <code>DistanceType.AHEAD</code> event.
That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SafetyCameraWarningListener">
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-safetycamerawarninglistener(void onSafetyCameraWarningUpdatedLambda(/sdk-for-flutter-navigate-navigation-safetycamerawarning-class))
</dt>
<dd>
          This abstract class
should be implemented in order to receive notifications on safety cameras.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-runtimetype
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
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onSafetyCameraWarningUpdated">
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-onsafetycamerawarningupdated(<wbr/>/sdk-for-flutter-navigate-navigation-safetycamerawarning-class safetyCameraWarning)
    → void

</dt>
<dd>
  Called whenever a new <code>SafetyCameraWarning</code> is available.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">SafetyCameraWarningListener class</li>
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



</div>
`
}</HTMLBlock>
