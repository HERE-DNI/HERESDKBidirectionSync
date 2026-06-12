---
title: "LocationIssueListener class abstract"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationIssueListener-class.html -->


<div>
<h1>LocationIssueListener class abstract</h1></div>

<p>abstract class receiving notifications when the set of
currently active location issues changes.</p>
<p>Location issues represent unexpected or degraded conditions affecting positioning quality,
availability, or functionality. The LocationEngine monitors various positioning subsystems
and aggregates detected issues into a unified snapshot delivered via this interface.</p>
<ul>
<li>Each callback delivers the complete current set of active issues.</li>
<li>An empty list indicates all previously reported issues have cleared.</li>
<li>Issues are transient by design and automatically removed once underlying conditions improve.
No explicit clear/dismiss API is provided.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-locationissuelistener">LocationIssueListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-onlocationissuechanged">onLocationIssueChanged</a></li><li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
