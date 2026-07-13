---
title: "TMCServiceInterface class - trafficbroadcast library - Dart API"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TMCServiceInterface-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficbroadcast/trafficbroadcast-library-sidebar.html" data-below-sidebar="trafficbroadcast/TMCServiceInterface-class-sidebar.html">

<div>

# <span class="kind-class">TMCServiceInterface</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Contains all outgoing dependencies to the client side.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-tmcserviceinterface">TMCServiceInterface</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-requestTMCServiceLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">requestTMCServiceLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcservicerequest-class">TMCServiceRequest</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-getTMCPreferredSidsLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">getTMCPreferredSidsLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcpreferredsidsrequest-class">TMCPreferredSidsRequest</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-getRDSEncryptionKeysLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-class">RDSEncryptionKey</a></span>\></span></span> <span class="parameter-name">getRDSEncryptionKeysLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkeysrequest-class">RDSEncryptionKeysRequest</a></span></span>)</span>)</span>  
Contains all outgoing dependencies to the client side.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-getrdsencryptionkeys">getRDSEncryptionKeys</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getRDSEncryptionKeys-param-rdsEncryptionKeysRequest" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkeysrequest-class">RDSEncryptionKeysRequest</a></span> <span class="parameter-name">rdsEncryptionKeysRequest</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-class">RDSEncryptionKey</a></span>\></span></span> </span>  
Called whenever there is a need to get RDS encryption keys.

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-gettmcpreferredsids">getTMCPreferredSids</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getTMCPreferredSids-param-tmcPreferredSidsRequest" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcpreferredsidsrequest-class">TMCPreferredSidsRequest</a></span> <span class="parameter-name">tmcPreferredSidsRequest</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> </span>  
Called whenever there is a need to get a list of preferred SIDs for a specific area.

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-requesttmcservice">requestTMCService</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-requestTMCService-param-tmcServiceRequest" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcservicerequest-class">TMCServiceRequest</a></span> <span class="parameter-name">tmcServiceRequest</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever the traffic broadcast needs to be activated.

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
