---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-heremap-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- HereMap-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">HereMap class</li>
</ol>
<div class="self-name">HereMap</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/HereMap-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>HereMap class</h1></div>
<section class="desc markdown">
<p>Widget that displays a map. To interact with the map, use the
/sdk-for-flutter-explore-mapview-heremapcontroller-class object that is passed to /sdk-for-flutter-explore-mapview-heremapcreatedcallback
Note: Before using this class, /sdk-for-flutter-explore-core-engine-sdknativeengine-class must be already initialized.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="HereMap">
/sdk-for-flutter-explore-mapview-heremap-heremap({Key? key, /sdk-for-flutter-explore-mapview-heremapcreatedcallback? onMapCreated, Set&lt;<wbr/>Factory&lt;<wbr/>OneSequenceGestureRecognizer&gt;&gt;? gestureRecognizers, /sdk-for-flutter-explore-mapview-nativeviewmode mode = NativeViewMode.virtualDisplay, dynamic options})
</dt>
<dd>
          Creates a widget that displays a map.
            <div class="constructor-modifier features">const</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="gestureRecognizers">
/sdk-for-flutter-explore-mapview-heremap-gesturerecognizers
→ Set&lt;<wbr/>Factory&lt;<wbr/>OneSequenceGestureRecognizer&gt;&gt;?
</dt>
<dd>
  Which gestures should be consumed by the map.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-heremap-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="key">
/sdk-for-flutter-explore-mapview-heremap-key
→ Key?
</dt>
<dd class="inherited">
  Controls how one widget replaces another widget in the tree.
  <div class="features">finalinherited</div>
</dd>
<dt class="property" id="mode">
/sdk-for-flutter-explore-mapview-heremap-mode
→ /sdk-for-flutter-explore-mapview-nativeviewmode
</dt>
<dd>
  Which method of hosting Android native view (the map) will be used.
Default value is /sdk-for-flutter-explore-mapview-nativeviewmode.
  <div class="features">final</div>
</dd>
<dt class="property" id="onMapCreated">
/sdk-for-flutter-explore-mapview-heremap-onmapcreated
→ /sdk-for-flutter-explore-mapview-heremapcreatedcallback?
</dt>
<dd>
  Method called when the map is ready to be used.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-heremap-runtimetype
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
<dt class="callable inherited" id="createElement">
/sdk-for-flutter-explore-mapview-heremap-createelement(<wbr/>)
    → StatefulElement

</dt>
<dd class="inherited">
  Creates a <code>StatefulElement</code> to manage this widget's location in the tree.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="createState">
/sdk-for-flutter-explore-mapview-heremap-createstate(<wbr/>)
    → State&lt;<wbr/>StatefulWidget&gt;

</dt>
<dd>
  Creates the mutable state for this widget at a given location in the tree.
  

</dd>
<dt class="callable inherited" id="debugDescribeChildren">
/sdk-for-flutter-explore-mapview-heremap-debugdescribechildren(<wbr/>)
    → List&lt;<wbr/>DiagnosticsNode&gt;

</dt>
<dd class="inherited">
  Returns a list of <code>DiagnosticsNode</code> objects describing this node's
children.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="debugFillProperties">
/sdk-for-flutter-explore-mapview-heremap-debugfillproperties(<wbr/>DiagnosticPropertiesBuilder properties)
    → void

</dt>
<dd class="inherited">
  Add additional properties associated with the node.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-heremap-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toDiagnosticsNode">
/sdk-for-flutter-explore-mapview-heremap-todiagnosticsnode(<wbr/>{String? name, DiagnosticsTreeStyle? style})
    → DiagnosticsNode

</dt>
<dd class="inherited">
  Returns a debug representation of the object that is used by debugging
tools and by <code>DiagnosticsNode.toStringDeep</code>.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-heremap-tostring(<wbr/>{DiagnosticLevel minLevel = DiagnosticLevel.info})
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toStringDeep">
/sdk-for-flutter-explore-mapview-heremap-tostringdeep(<wbr/>{String prefixLineOne = '', String? prefixOtherLines, DiagnosticLevel minLevel = DiagnosticLevel.debug, int wrapWidth = 65})
    → String

</dt>
<dd class="inherited">
  Returns a string representation of this node and its descendants.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toStringShallow">
/sdk-for-flutter-explore-mapview-heremap-tostringshallow(<wbr/>{String joiner = ', ', DiagnosticLevel minLevel = DiagnosticLevel.debug})
    → String

</dt>
<dd class="inherited">
  Returns a one-line detailed description of the object.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toStringShort">
/sdk-for-flutter-explore-mapview-heremap-tostringshort(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A short, textual description of this widget.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-heremap-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">HereMap class</li>
</ol>
<h5>mapview library</h5>
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
