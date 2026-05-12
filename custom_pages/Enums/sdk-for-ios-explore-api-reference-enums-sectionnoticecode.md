---
title: "SectionNoticeCode Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-sectionnoticecode"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SectionNoticeCode.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/SectionNoticeCode"></a>
<a title="SectionNoticeCode Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SectionNoticeCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum SectionNoticeCode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Notice codes which point the issues encountered during processing of a <code><a href="../Classes/Section.html">Section</a></code>.</p>
<p><strong>Note:</strong> The section notice codes are going to be extended for new error situations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO20violatedCriticalRuleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedCriticalRule"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO20violatedCriticalRuleyA2CmF">violatedCriticalRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route has violoated a non-detailed critical rule.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedCriticalRule</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO36violatedAvoidControlledAccessHighwayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidControlledAccessHighway"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO36violatedAvoidControlledAccessHighwayyA2CmF">violatedAvoidControlledAccessHighway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidControlledAccessHighway</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO21violatedAvoidTollRoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidTollRoad"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO21violatedAvoidTollRoadyA2CmF">violatedAvoidTollRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidTollRoad</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO18violatedAvoidFerryyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidFerry"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO18violatedAvoidFerryyA2CmF">violatedAvoidFerry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidFerry</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO19violatedAvoidTunnelyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidTunnel"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO19violatedAvoidTunnelyA2CmF">violatedAvoidTunnel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidTunnel</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO21violatedAvoidDirtRoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidDirtRoad"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO21violatedAvoidDirtRoadyA2CmF">violatedAvoidDirtRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidDirtRoad</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO22violatedAvoidRailFerryyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidRailFerry"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO22violatedAvoidRailFerryyA2CmF">violatedAvoidRailFerry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidRailFerry</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO17violatedAvoidParkyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidPark"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO17violatedAvoidParkyA2CmF">violatedAvoidPark</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidPark</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedBlockedRoad"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">violatedBlockedRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route uses roads blocked by traffic events or
route did not manage to avoid the requested
<code>avoidBoundingBoxAreas</code> or <code>countries</code> or <code>segments</code>.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedBlockedRoad</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO22violatedStartDirectionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedStartDirection"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO22violatedStartDirectionyA2CmF">violatedStartDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start direction of the route is not as requested.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedStartDirection</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO15violatedCarpoolyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedCarpool"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO15violatedCarpoolyA2CmF">violatedCarpool</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid user preference.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedCarpool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO23violatedTurnRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedTurnRestriction"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO23violatedTurnRestrictionyA2CmF">violatedTurnRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route uses a time-restricted turn.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedTurnRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO26violatedVehicleRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedVehicleRestriction"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO26violatedVehicleRestrictionyA2CmF">violatedVehicleRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route uses a road which is forbidden for the given vehicle profile.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedVehicleRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO23violatedZoneRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedZoneRestriction"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO23violatedZoneRestrictionyA2CmF">violatedZoneRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route uses a road which is part of restricted <code>zoneCategories</code>
requested to be avoided by user.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedZoneRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO19violatedAvoidUTurnsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidUTurns"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO19violatedAvoidUTurnsyA2CmF">violatedAvoidUTurns</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid u turns.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidUTurns</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO21violatedEmergencyGateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedEmergencyGate"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO21violatedEmergencyGateyA2CmF">violatedEmergencyGate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route goes through an emergency gate.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedEmergencyGate</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO28violatedAvoidSeasonalClosureyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidSeasonalClosure"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO28violatedAvoidSeasonalClosureyA2CmF">violatedAvoidSeasonalClosure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid seasonal closure.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidSeasonalClosure</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO26violatedAvoidTruckRoadTypeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidTruckRoadType"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO26violatedAvoidTruckRoadTypeyA2CmF">violatedAvoidTruckRoadType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid restricted truck road types.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidTruckRoadType</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO28violatedAvoidTollTransponderyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidTollTransponder"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO28violatedAvoidTollTransponderyA2CmF">violatedAvoidTollTransponder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid toll booth that requires transponder.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidTollTransponder</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO35violatedChargingStationOpeningHoursyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedChargingStationOpeningHours"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO35violatedChargingStationOpeningHoursyA2CmF">violatedChargingStationOpeningHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging at the charging station planned at the destination of this section falls outside of opening hours.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedChargingStationOpeningHours</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO27violatedAvoidDifficultTurnsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedAvoidDifficultTurns"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO27violatedAvoidDifficultTurnsyA2CmF">violatedAvoidDifficultTurns</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route did not manage to avoid difficult turns.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO8criticalyA2CmF">NoticeSeverity.critical</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedAvoidDifficultTurns</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO15seasonalClosureyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/seasonalClosure"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO15seasonalClosureyA2CmF">seasonalClosure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route goes through seasonal closure.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case seasonalClosure</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO15tollTransponderyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tollTransponder"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO15tollTransponderyA2CmF">tollTransponder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route goes through toll booth that requires transponder.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case tollTransponder</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO20tollsDataUnavailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tollsDataUnavailable"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO20tollsDataUnavailableyA2CmF">tollsDataUnavailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tolls data was requested but could not be calculated for this section.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case tollsDataUnavailable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO31tollsDataTemporarilyUnavailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tollsDataTemporarilyUnavailable"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO31tollsDataTemporarilyUnavailableyA2CmF">tollsDataTemporarilyUnavailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tolls data was requested but is temporarily unavailable.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case tollsDataTemporarilyUnavailable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO21chargingStopNotNeededyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/chargingStopNotNeeded"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO21chargingStopNotNeededyA2CmF">chargingStopNotNeeded</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A charging stop was planned at the destination of this section, but it is no longer
needed. It may be issued only when refreshing a route via <code><a href="../Structs/RouteHandle.html">RouteHandle</a></code>.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case chargingStopNotNeeded</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO10noScheduleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noSchedule"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO10noScheduleyA2CmF">noSchedule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No schedule information is available for a transit section. As a result, departure/arrival times are approximated.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case noSchedule</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO14noIntermediateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noIntermediate"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO14noIntermediateyA2CmF">noIntermediate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Information about intermediate stops is not available for a transit section.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case noIntermediate</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO12unwantedModeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unwantedMode"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO12unwantedModeyA2CmF">unwantedMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This transit section contains a transport mode that was explictly disabled.
Mode filtering is not available in this area.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case unwantedMode</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO14scheduledTimesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/scheduledTimes"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO14scheduledTimesyA2CmF">scheduledTimes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This transit section returned times which are scheduled times, even though delay information is available.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case scheduledTimes</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO14simplePolylineyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/simplePolyline"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO14simplePolylineyA2CmF">simplePolyline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An accurate polyline is not available for this section. An accurate polyline is not available for this
section. The returned polyline has been generated from departure and arrival places.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case simplePolyline</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO16potentialCarpoolyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/potentialCarpool"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO16potentialCarpoolyA2CmF">potentialCarpool</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route utilizes a designated carpool lane, potentially subject to restrictions beyond the scheduled travel hours.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case potentialCarpool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO24potentialTurnRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/potentialTurnRestriction"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO24potentialTurnRestrictionyA2CmF">potentialTurnRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route includes a turn that is potentially restricted and inaccessible beyond the scheduled travel hours.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case potentialTurnRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO27potentialVehicleRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/potentialVehicleRestriction"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO27potentialVehicleRestrictionyA2CmF">potentialVehicleRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route utilizes roads that are potentially off-limits to the specified vehicle profile beyond the scheduled travel hours.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case potentialVehicleRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO24potentialZoneRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/potentialZoneRestriction"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO24potentialZoneRestrictionyA2CmF">potentialZoneRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route incorporates roads within zones, which are potentially not accessible beyond the scheduled travel hours.
Severity: <code><a href="../Enums/NoticeSeverity.html#/s:7heresdk14NoticeSeverityO4infoyA2CmF">NoticeSeverity.info</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case potentialZoneRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO26violatedMinChargeAtFirstCsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedMinChargeAtFirstCs"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO26violatedMinChargeAtFirstCsyA2CmF">violatedMinChargeAtFirstCs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route can not reach the first charging station with the minimum required charge, as the initial charge was to low.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedMinChargeAtFirstCs</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO21violatedMinChargeAtCsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedMinChargeAtCs"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO21violatedMinChargeAtCsyA2CmF">violatedMinChargeAtCs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route can not reach all charging stations on the route with the minimum required charge, as the initial charge was to low.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedMinChargeAtCs</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO30violatedMinChargeAtDestinationyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/violatedMinChargeAtDestination"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO30violatedMinChargeAtDestinationyA2CmF">violatedMinChargeAtDestination</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route can not reach the waypoint, as the there are not enough charging stops available or the initial charge was to low.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case violatedMinChargeAtDestination</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SectionNoticeCodeO20noThroughRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noThroughRestriction"></a>
<a class="token" href="#/s:7heresdk17SectionNoticeCodeO20noThroughRestrictionyA2CmF">noThroughRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route goes through a road that does not allow through traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case noThroughRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>
