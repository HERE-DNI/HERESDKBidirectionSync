---
title: "LocationSource Enumeration Reference"
slug: "sdk-for-ios-navigate-locationsource"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- LocationSource.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>LocationSource Enumeration Reference</title>
    <link rel="stylesheet" type="text/css" href="../css/jazzy.css" />
    <link rel="stylesheet" type="text/css" href="../css/highlight.css" />
    <meta charset='utf-8'>
    <script src="../js/jquery.min.js" defer></script>
    <script src="../js/jazzy.js" defer></script>
    
    <script src="../js/lunr.min.js" defer></script>
    <script src="../js/typeahead.jquery.js" defer></script>
    <script src="../js/jazzy.search.js" defer></script>
  </head>
  <body>
    <a name="//apple_ref/swift/Enum/LocationSource" class="dashAnchor"></a>
    <a title="LocationSource Enumeration Reference"></a>
    <header>
      <div class="content-wrapper">
        <p><a href="sdk-for-ios-explore-index">heresdk Docs</a> (99% documented)</p>
        <div class="header-right">
          <form role="search" action="../search.json">
            <input type="text" placeholder="Search documentation" data-typeahead>
          </form>
        </div>
      </div>
    </header>
    <div class="content-wrapper">
      <p id="breadcrumbs">
        <a href="sdk-for-ios-explore-index">heresdk</a>
        <img id="carat" src="../img/carat.png" alt=""/>
        <a href="sdk-for-ios-explore-core">Core</a>
        <img id="carat" src="../img/carat.png" alt=""/>
        LocationSource Enumeration Reference
      </p>
    </div>
    <div class="content-wrapper">
      <nav class="sidebar">
        <ul class="nav-groups">
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-core">Core</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-anchor2d">Anchor2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-anchor2dkeyframe">Anchor2DKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-angle">Angle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-anglerange">AngleRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authentication">Authentication</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk23AuthenticationExceptiona">AuthenticationException</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authenticationmode">AuthenticationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-brandlogo">BrandLogo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk30CacheCallbackCompletionHandlera">CacheCallbackCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-cardinaldirection">CardinalDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogconfiguration">CatalogConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogidentifier">CatalogIdentifier</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogtype">CatalogType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogupdatetask">CatalogUpdateTask</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogversionhint">CatalogVersionHint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-collectionof">CollectionOf</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-countrycode">CountryCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-currenttype">CurrentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-custommetadatavalue">CustomMetadataValue</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-desiredcatalog">DesiredCatalog</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk14DeviceIdHandlea">DeviceIdHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-enginebaseurl">EngineBaseURL</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-engineoptions">EngineOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-externalid">ExternalID</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geobox">GeoBox</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocircle">GeoCircle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocoordinates">GeoCoordinates</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocoordinatesupdate">GeoCoordinatesUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocorridor">GeoCorridor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoorientation">GeoOrientation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoorientationupdate">GeoOrientationUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geopolygon">GeoPolygon</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geopolyline">GeoPolyline</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geopolylinedirection">GeoPolylineDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">InstantiationError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-integerrange">IntegerRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-junctionstraversability">JunctionsTraversability</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-languagecode">LanguageCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-layerconfiguration">LayerConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-feature">– Feature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedroadnumber">LocalizedRoadNumber</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedroadnumbers">LocalizedRoadNumbers</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedtext">LocalizedText</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedtexts">LocalizedTexts</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-location">Location</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationdelegate">LocationDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationsource">LocationSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationtechnology">LocationTechnology</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationtime">LocationTime</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-logappender">LogAppender</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-logcontrol">LogControl</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-loglevel">LogLevel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-metadata">Metadata</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-metadatatype">MetadataType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-nameid">NameID</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-networkendpoint">NetworkEndpoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-networksettings">NetworkSettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-parameterconfiguration">ParameterConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-passthroughfeature">PassThroughFeature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-powertype">PowerType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianprofile">PedestrianProfile</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pickedplace">PickedPlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-platformthreading">PlatformThreading</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-point2d">Point2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-point3d">Point3D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polylinesimplificationerror">PolylineSimplificationError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polylinesimplifier">PolylineSimplifier</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-options">– Options</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-proxysettings">ProxySettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-proxytype">– ProxyType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-credentials">– Credentials</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rectangle2d">Rectangle2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routetype">RouteType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-runnable">Runnable</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkbuildinformation">SDKBuildInformation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkcache">SDKCache</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkinternalinitializer">SDKInternalInitializer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdklogger">SDKLogger</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdknativeengine">SDKNativeEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-purgememorystrategy">– PurgeMemoryStrategy</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs)SDKNativeEngineHolder">SDKNativeEngineHolder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkoptions">SDKOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkversion">SDKVersion</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-size2d">Size2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:SS">String</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taskhandle">TaskHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taskoutcome">TaskOutcome</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-threading">Threading</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-timerule">TimeRule</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transportprofile">TransportProfile</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-uicolor">UIColor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-unitsystem">UnitSystem</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-usagestats">UsageStats</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-feature">– Feature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-networkstats">– NetworkStats</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-electronichorizon">ElectronicHorizon</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizon">ElectronicHorizon</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizondataloader">ElectronicHorizonDataLoader</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizondataloadererrorcode">ElectronicHorizonDataLoaderErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizondataloaderresult">ElectronicHorizonDataLoaderResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizondelegate">ElectronicHorizonDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonengine">ElectronicHorizonEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonoptions">ElectronicHorizonOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonpath">ElectronicHorizonPath</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonposition">ElectronicHorizonPosition</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonsegment">ElectronicHorizonSegment</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonsegmentid">ElectronicHorizonSegmentId</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electronichorizonupdate">ElectronicHorizonUpdate</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-ev">EV</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectorformat">EVChargingConnectorFormat</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectortype">EVChargingConnectorType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsecapability">EVSECapability</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsepaymentsupport">EVSEPaymentSupport</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsestate">EVSEState</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-positioning">Positioning</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authenticationdata">AuthenticationData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authenticationerror">AuthenticationError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-confirmationstatus">ConfirmationStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationaccuracy">LocationAccuracy</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationenginebase">LocationEngineBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationenginestatus">LocationEngineStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationfeature">LocationFeature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationengine">LocationEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationsimulator">LocationSimulator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationsimulatoroptions">LocationSimulatorOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationstatusdelegate">LocationStatusDelegate</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-mapdata">MapData</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-administrativerules">AdministrativeRules</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-administrativerulesloader">AdministrativeRulesLoader</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-allowedtransportmodes">AllowedTransportModes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-connectivity">Connectivity</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-directedocmsegmentid">DirectedOCMSegmentId</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-downloadingfileoptions">DownloadingFileOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-drivingside">DrivingSide</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-filereference">FileReference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-filereferencetype">FileReferenceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-headlightsrequirement">HeadlightsRequirement</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-laneattribute">LaneAttribute</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localroadcharacteristic">LocalRoadCharacteristic</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapdata#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapdataloadererrorcode">MapDataLoaderErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-ocmsegmentid">OCMSegmentId</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-parkingsideregulation">ParkingSideRegulation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-physicalattributes">PhysicalAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pretripplanning">PreTripPlanning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-railwaycrossing">RailwayCrossing</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-railwaycrossingtype">RailwayCrossingType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roaddivider">RoadDivider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadusages">RoadUsages</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentconnectivities">SegmentConnectivities</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentdata">SegmentData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentdataloader">SegmentDataLoader</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentdataloaderoptions">SegmentDataLoaderOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentreferenceconverter">SegmentReferenceConverter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentspandata">SegmentSpanData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentspecialspeedsituation">SegmentSpecialSpeedSituation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentspeedlimit">SegmentSpeedLimit</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-specialspeedtype">SpecialSpeedType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollcost">TollCost</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollpoint">TollPoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollstructure">TollStructure</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollstructuremaneuver">TollStructureManeuver</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollstructuretype">TollStructureType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollsystem">TollSystem</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficsignal">TrafficSignal</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficsignallocation">TrafficSignalLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-turnonredregulation">TurnOnRedRegulation</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-maploader">MapLoader</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogupdateinfo">CatalogUpdateInfo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogupdateprogresslistener">CatalogUpdateProgressListener</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogupdatestate">CatalogUpdateState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-clientcertificaterequesttype">ClientCertificateRequestType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk17CompletionHandlera">CompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributesbase">DataAttributesBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk30DeleteRegionsCompletionHandlera">DeleteRegionsCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-downloadregionsstatuslistener">DownloadRegionsStatusListener</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-externalmapdatasourceclient">ExternalMapDataSourceClient</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk35ExternalMapDataSourceExceptionErrora">ExternalMapDataSourceExceptionError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-externalmapdatasourceserver">ExternalMapDataSourceServer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-installedcatalog">InstalledCatalog</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-installedregion">InstalledRegion</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-installedregionstatus">InstalledRegionStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk8LineDataC">LineData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedataaccessor">LineDataAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedatabuilder">LineDataBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedatasource">LineDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedatasourcebuilder">LineDataSourceBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploadererror">MapLoaderError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapdownloader">MapDownloader</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk31MapDownloaderConstructionHandlea">MapDownloaderConstructionHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapdownloadertask">MapDownloaderTask</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapupdateprogresslistener">MapUpdateProgressListener</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapupdater">MapUpdater</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapupdateversioncommitpolicy">– MapUpdateVersionCommitPolicy</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk29MapUpdaterConstructionHandlera">MapUpdaterConstructionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapupdatetask">MapUpdateTask</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapversionhandle">MapVersionHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-navigabilitytype">NavigabilityType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk25OfflineStorageSizeHandlera">OfflineStorageSizeHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk23RepairCompletionHandlera">RepairCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pemkeycertpair">PemKeyCertPair</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-persistentmaprepairerror">PersistentMapRepairError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-persistentmapstatus">PersistentMapStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-region">Region</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-regionid">RegionId</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk19ServerStartedHandlea">ServerStartedHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sslclientcredentialsoptions">SslClientCredentialsOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sslservercredentialsoptions">SslServerCredentialsOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-updatestatistics">UpdateStatistics</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-mapmatcher">MapMatcher</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmatcher">MapMatcher</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-matchedlocation">MatchedLocation</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-maps">Maps</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-animationdelegate">AnimationDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-animationstate">AnimationState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-assetsmanager">AssetsManager</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributes">DataAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributesaccessor">DataAttributesAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributesbuilder">DataAttributesBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributevalue">DataAttributeValue</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-valuetype">– ValueType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dashpattern">DashPattern</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-doubletapdelegate">DoubleTapDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-drawordertype">DrawOrderType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-easing">Easing</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-easingfunction">EasingFunction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoorientationkeyframe">GeoOrientationKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gesturestate">GestureState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gesturetype">GestureType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gestures">Gestures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-heremap">HereMap</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-iconprovider">IconProvider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-iconproviderassettype">IconProviderAssetType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk20IconProviderCallbacka">IconProviderCallback</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-iconprovidererror">IconProviderError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-imageformat">ImageFormat</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-jsonstylefactory">JsonStyleFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrordetails">– InstantiationErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-keyframeinterpolationmode">KeyframeInterpolationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linecap">LineCap</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linetiledatasource">LineTileDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linetilesource">LineTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linetilesourceloadresulthandler">LineTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationindicator">LocationIndicator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indicatorstyle">– IndicatorStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-markertype">– MarkerType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-longpressdelegate">LongPressDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maparrow">MapArrow</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcamera">MapCamera</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-state">– State</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farplaneconfiguration">– FarPlaneConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraanimation">MapCameraAnimation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraanimationfactory">MapCameraAnimationFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameradelegate">MapCameraDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameralimits">MapCameraLimits</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraupdate">MapCameraUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraupdatefactory">MapCameraUpdateFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontentcategory">MapContentCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontentsettings">MapContentSettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficrefreshperioderrorcode">– TrafficRefreshPeriodErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontenttype">MapContentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontext">MapContext</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementstrategy">– MemoryManagementStrategy</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementresultcode">– MemoryManagementResultCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-resourcetype">– ResourceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-freeresourceseverity">– FreeResourceSeverity</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementresult">– MemoryManagementResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementoptions">– MemoryManagementOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maperror">MapError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapfeatures">MapFeatures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapfeaturemodes">MapFeatureModes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapidledelegate">MapIdleDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapimage">MapImage</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapimageoverlay">MapImageOverlay</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapitemkeyframetrack">MapItemKeyFrameTrack</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk21MapItemRepresentationC">MapItemRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayer">MapLayer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayerbuilder">MapLayerBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrordetails">– InstantiationErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayerprioritybuilder">MapLayerPriorityBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayermapmeasuredependentstoragelevels">MapLayerMapMeasureDependentStorageLevels</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayervisibilityrange">MapLayerVisibilityRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarkercluster">MapMarkerCluster</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-grouping">– Grouping</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-imagestyle">– ImageStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-counterstyle">– CounterStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmeasurerange">MapMeasureRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapobjectdescriptor">MapObjectDescriptor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapprojection">MapProjection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapscenelights">MapSceneLights</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-category">– Category</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-attributesettingerror">– AttributeSettingError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-direction">– Direction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrordetails">– InstantiationErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarker">MapMarker</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-textstyle">– TextStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarker3d">MapMarker3D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarker3dmodel">MapMarker3DModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarkeranimation">MapMarkerAnimation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmeasure">MapMeasure</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-kind">– Kind</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappolygon">MapPolygon</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappolyline">MapPolyline</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-representation">– Representation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dashimagerepresentation">– DashImageRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-solidrepresentation">– SolidRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dashrepresentation">– DashRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-solidmulticolorrepresentation">– SolidMultiColorRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappolylineanimation">MapPolylineAnimation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappickresult">MapPickResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapscene">MapScene</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappickfilter">– MapPickFilter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapscheme">MapScheme</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapviewbase">MapViewBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapview">MapView</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-viewpin">– ViewPin</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapviewoptions">MapViewOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-materialreflectivity">MaterialReflectivity</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk4MeshC">Mesh</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-meshbuilder">MeshBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pandelegate">PanDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pickmapcontentresult">PickMapContentResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentresult">– TrafficIncidentResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestrictionresult">– VehicleRestrictionResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pickmapitemsresult">PickMapItemsResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pinchrotatedelegate">PinchRotateDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk9PointDataC">PointData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdataaccessor">PointDataAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdatabuilder">PointDataBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdatasource">PointDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdatasourcebuilder">PointDataSourceBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointtiledatasource">PointTileDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointtilesource">PointTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointtilesourceloadresulthandler">PointTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-point2dkeyframe">Point2DKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk11PolygonDataC">PolygonData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondataaccessor">PolygonDataAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondatabuilder">PolygonDataBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondatasource">PolygonDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondatasourcebuilder">PolygonDataSourceBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygontiledatasource">PolygonTileDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygontilesource">PolygonTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygontilesourceloadresulthandler">PolygonTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-quadmeshbuilder">QuadMeshBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasource">RasterDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-provider">– Provider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-cache">– Cache</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourceconfigurationupdate">RasterDataSourceConfigurationUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourcedelegate">RasterDataSourceDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourceerror">RasterDataSourceError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rastertilesource">RasterTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rastertilesourceloadresulthandler">RasterTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadshieldiconproperties">RoadShieldIconProperties</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rendersize">RenderSize</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-unit">– Unit</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scalarkeyframe">ScalarKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkmapviewinitializer">SDKMapViewInitializer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-shadowquality">ShadowQuality</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-style">Style</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tapdelegate">TapDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilegeoboundscalculator">TileGeoBoundsCalculator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesource">TileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourcedataversion">TileSourceDataVersion</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourcedelegate">TileSourceDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourceloadtilerequesthandle">TileSourceLoadTileRequestHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourcetilemetadata">TileSourceTileMetadata</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilekey">TileKey</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tileurlproviderfactory">TileUrlProviderFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilingscheme">TilingScheme</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-translucentmaplayergroup">TranslucentMapLayerGroup</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-errorcode">– ErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-errordetails">– ErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trianglemeshbuilder">TriangleMeshBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-twofingerpandelegate">TwoFingerPanDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-twofingertapdelegate">TwoFingerTapDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-visibilitystate">VisibilityState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestrictioniconproperties">VehicleRestrictionIconProperties</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-watermarkstyle">WatermarkStyle</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-routing">Routing</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-accessattributes">AccessAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-agency">Agency</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-allowoptions">AllowOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-attribution">Attribution</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-attributiontype">AttributionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidanceoptions">AvoidanceOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidboundingboxareaoptions">AvoidBoundingBoxAreaOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidcorridorareaoptions">AvoidCorridorAreaOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-batteryspecifications">BatterySpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bicycleoptions">BicycleOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busoptions">BusOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-caroptions">CarOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routing#/s:7heresdk37CalculateIndoorRouteCompletionHandlera">CalculateIndoorRouteCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routing#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routing#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routing#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingactiondetails">ChargingActionDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingconnectorattributes">ChargingConnectorAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingconnectortype">ChargingConnectorType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-key">– Key</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-codingerror">– CodingError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingstation">ChargingStation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingstop">ChargingStop</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingsupplytype">ChargingSupplyType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dynamicspeedinfo">DynamicSpeedInfo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electricvehicleoptions">ElectricVehicleOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-empiricalconsumptionmodel">EmpiricalConsumptionModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evcaroptions">EVCarOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingpool">EVChargingPool</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingstation">EVChargingStation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evconsumptionmodel">EVConsumptionModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evtruckoptions">EVTruckOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fare">Fare</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farepassvalidityperiod">FarePassValidityPeriod</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farepassvalidityperiodtype">FarePassValidityPeriodType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fareprice">FarePrice</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farepricetype">FarePriceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farereason">FareReason</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-functionalroadclass">FunctionalRoadClass</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-hazardousmaterial">HazardousMaterial</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indooravoidanceoptions">IndoorAvoidanceOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoormaneuver">IndoorManeuver</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorrouteoptions">IndoorRouteOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorroutestyle">IndoorRouteStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorroutingcontroller">IndoorRoutingController</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorroutingengine">IndoorRoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorroutingerror">IndoorRoutingError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorwaypoint">IndoorWaypoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isoline">Isoline</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolinecalculationmode">IsolineCalculationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolineoptions">IsolineOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-calculation">– Calculation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolinerangetype">IsolineRangeType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolineroutingengine">IsolineRoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedtextpreference">LocalizedTextPreference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuver">Maneuver</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuveraction">ManeuverAction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapdatasize">MapDataSize</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapdatasizelistener">MapDataSizeListener</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmatchedcoordinates">MapMatchedCoordinates</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-matchsideofstreet">MatchSideOfStreet</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maxaxlegroupweight">MaxAxleGroupWeight</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maxspeedonsegment">MaxSpeedOnSegment</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-noticeseverity">NoticeSeverity</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offlineroutingengine">OfflineRoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offlineroutingengineoptions">OfflineRoutingEngineOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-optimizationmode">OptimizationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-passthroughwaypoint">PassThroughWaypoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-paymentmethod">PaymentMethod</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianoptions">PedestrianOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-physicalconsumptionmodel">PhysicalConsumptionModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygonprefetcher">PolygonPrefetcher</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-postaction">PostAction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-postactiondelegate">PostActionDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-postactiontype">PostActionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-preaction">PreAction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-preactiontype">PreActionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-prefetchstatuslistener">PrefetchStatusListener</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-privatebusoptions">PrivateBusOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-refreshrouteoptions">RefreshRouteOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadattributes">RoadAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadattributesdelegate">RoadAttributesDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadfeatures">RoadFeatures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadtexts">RoadTexts</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-route">Route</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routehandle">RouteHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routelabel">RouteLabel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routelabeltype">RouteLabelType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeoffset">RouteOffset</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeoptions">RouteOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeplace">RoutePlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeplacedirection">RoutePlaceDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeplacetype">RoutePlaceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeprefetcher">RoutePrefetcher</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routerailwaycrossing">RouteRailwayCrossing</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routerailwaycrossingtype">RouteRailwayCrossingType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routestop">RouteStop</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routetextoptions">RouteTextOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingconnectionsettings">RoutingConnectionSettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingengine">RoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingerror">RoutingError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingoptions">RoutingOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingprotocol">RoutingProtocol</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooteroptions">ScooterOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-section">Section</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sectionnotice">SectionNotice</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sectionnoticecode">SectionNoticeCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sectiontransportmode">SectionTransportMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentreference">SegmentReference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sideofdestination">SideOfDestination</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-signpost">Signpost</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-signpostlabel">SignpostLabel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-streetattributes">StreetAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-span">Span</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxioptions">TaxiOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-textusageoptions">TextUsageOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-toll">Toll</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollfare">TollFare</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollfarepass">TollFarePass</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tolloptions">TollOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclecategory">– VehicleCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-emissiontype">– EmissionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficonroute">TrafficOnRoute</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficonspan">TrafficOnSpan</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficonsection">TrafficOnSection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitdeparture">TransitDeparture</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitdeparturestatus">TransitDepartureStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitincident">TransitIncident</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitincidenteffect">TransitIncidentEffect</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitincidenttype">TransitIncidentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitmode">TransitMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitmodefilter">TransitModeFilter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficoptimizationmode">TrafficOptimizationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitrouteoptions">TransitRouteOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitroutingengine">TransitRoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitsectiondetails">TransitSectionDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitstop">TransitStop</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transittransport">TransitTransport</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitwaypoint">TransitWaypoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traveldirection">TravelDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckoptions">TruckOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckspecifications">TruckSpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trucktype">TruckType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tunnelcategory">TunnelCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype">VehicleRestrictionMaxWeightType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclespecification">VehicleSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-carbuilder">– CarBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckbuilder">– TruckBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooterbuilder">– ScooterBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxibuilder">– TaxiBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busbuilder">– BusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-privatebusbuilder">– PrivateBusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-violatedrestriction">ViolatedRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-details">– Details</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-walkattributes">WalkAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-waypoint">Waypoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-waypointtype">WaypointType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-zonecategory">ZoneCategory</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-navigation">Navigation</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-areacamerabehavior">AreaCameraBehavior</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-arrivalnotificationoption">ArrivalNotificationOption</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-aspectratio">AspectRatio</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-automotivecamerabehavior">AutomotiveCameraBehavior</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-orientationmode">– OrientationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-activecameratype">– ActiveCameraType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bordercrossingtype">BorderCrossingType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bordercrossingwarning">BorderCrossingWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bordercrossingwarningoptions">BorderCrossingWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-camerabehavior">CameraBehavior</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-currentsituationlaneview">CurrentSituationLaneView</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-currentsituationlaneassistanceview">CurrentSituationLaneAssistanceView</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-custompanningdata">CustomPanningData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dangerzonewarning">DangerZoneWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dangerzonewarningdelegate">DangerZoneWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-destinationreacheddelegate">DestinationReachedDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dimensionrestriction">DimensionRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dimensionrestrictiontype">DimensionRestrictionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-directioninformationusageoption">DirectionInformationUsageOption</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-distancetype">DistanceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dividermarker">DividerMarker</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dynamiccamerabehavior">DynamicCameraBehavior</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dynamicroutingengine">DynamicRoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-starterror">– StartError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dynamicroutingdelegate">DynamicRoutingDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-environmentalzonewarning">EnvironmentalZoneWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-eventtext">EventText</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-eventtextdelegate">EventTextDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-eventtextoptions">EventTextOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fixedcamerabehavior">FixedCameraBehavior</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-generalwarningroadsigntype">GeneralWarningRoadSignType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gpxdocument">GPXDocument</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gpxoptions">GPXOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gpxtrack">GPXTrack</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gpxtrackwriter">GPXTrackWriter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-interpolatedlocationdelegate">InterpolatedLocationDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-junctionviewlaneassistance">JunctionViewLaneAssistance</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lane">Lane</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-laneaccess">LaneAccess</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lanedirection">LaneDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lanedirectioncategory">LaneDirectionCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lanemarkings">LaneMarkings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lanerecommendationstate">LaneRecommendationState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lanetype">LaneType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lowspeedzonewarning">LowSpeedZoneWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuvernotificationdetails">ManeuverNotificationDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuvernotificationoptions">ManeuverNotificationOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuvernotificationtype">ManeuverNotificationType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuverprogress">ManeuverProgress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmatchedlocation">MapMatchedLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-milestone">Milestone</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-milestonestatus">MilestoneStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-milestonestatusdelegate">MilestoneStatusDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-milestonetype">MilestoneType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-naturalguidancetype">NaturalGuidanceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-navigablelocation">NavigableLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-navigablelocationdelegate">NavigableLocationDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-navigator">Navigator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-navigatorprotocol">NavigatorProtocol</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-notificationformatoption">NotificationFormatOption</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offroadprogress">OffRoadProgress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offroadprogressdelegate">OffRoadProgressDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-realisticviewrasterimage">RealisticViewRasterImage</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-realisticviewvectorimage">RealisticViewVectorImage</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-realisticviewwarning">RealisticViewWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-realisticviewwarningdelegate">RealisticViewWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-realisticviewwarningoptions">RealisticViewWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-railwaycrossingwarning">RailwayCrossingWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadclassification">RoadClassification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadsign">RoadSign</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadsigncategory">RoadSignCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadsigntype">RoadSignType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadsignwarning">RoadSignWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadsignwarningdelegate">RoadSignWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadsignwarningoptions">RoadSignWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadsignvehicletype">RoadSignVehicleType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadtextsdelegate">RoadTextsDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routedeviation">RouteDeviation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routedeviationdelegate">RouteDeviationDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routematchedlocation">RouteMatchedLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeprogress">RouteProgress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeprogresscolors">RouteProgressColors</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeprogressdelegate">RouteProgressDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-safetycameratype">SafetyCameraType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-safetycamerawarning">SafetyCameraWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-safetycamerawarningoptions">SafetyCameraWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-schoolzonewarning">SchoolZoneWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-schoolzonewarningoptions">SchoolZoneWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdknavigationinitializer">SDKNavigationInitializer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sectionprogress">SectionProgress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-spatialaudiocuepanning">SpatialAudioCuePanning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-spatialnotificationdetails">SpatialNotificationDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-spatialtrajectorydata">SpatialTrajectoryData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedbasedcamerabehavior">SpeedBasedCameraBehavior</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-profilevalue">– ProfileValue</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedlimit">SpeedLimit</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedlimitdelegate">SpeedLimitDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedlimitoffset">SpeedLimitOffset</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedwarningdelegate">SpeedWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedwarningoptions">SpeedWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedwarningstatus">SpeedWarningStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-textnotificationtype">TextNotificationType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-timingprofile">TimingProfile</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollbooth">TollBooth</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollboothlane">TollBoothLane</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollcollectionmethod">TollCollectionMethod</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollstop">TollStop</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollstopwarningdelegate">TollStopWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trackingcamerabehavior">TrackingCameraBehavior</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-zoompolicy">– ZoomPolicy</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedthreshold">– SpeedThreshold</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-functionalroadclasszoompolicyoptions">– FunctionalRoadClassZoomPolicyOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-speedbasedzoompolicyoptions">– SpeedBasedZoomPolicyOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuverzoomrange">– ManeuverZoomRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuverruleoptions">– ManeuverRuleOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuverrule">– ManeuverRule</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuvermodeconfiguration">– ManeuverModeConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficmergeroadtype">TrafficMergeRoadType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficmergeside">TrafficMergeSide</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficmergewarning">TrafficMergeWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficmergewarningoptions">TrafficMergeWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficonroutecolors">TrafficOnRouteColors</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckrestrictionwarning">TruckRestrictionWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-visualnavigator">VisualNavigator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-visualnavigatorcolors">VisualNavigatorColors</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-wallclock">WallClock</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-warningnotificationdistances">WarningNotificationDistances</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-warningtype">WarningType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-weathertype">WeatherType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-weightrestriction">WeightRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-weightrestrictiontype">WeightRestrictionType</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-search">Search</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-address">Address</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-addresstype">AddressType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-addressquery">AddressQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-areatype">AreaType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-businessdetails">BusinessDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-categoryquery">CategoryQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-area">– Area</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-contact">Contact</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-daterange">DateRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dayofweek">DayOfWeek</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-details">Details</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-emailaddress">EmailAddress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-emobilityserviceprovider">EMobilityServiceProvider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-energymix">EnergyMix</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-energysource">EnergySource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-energysourcetype">EnergySourceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-environmentalimpact">EnvironmentalImpact</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-environmentalimpactcategory">EnvironmentalImpactCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evaccessrestrictionreason">EVAccessRestrictionReason</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evaccesstype">EVAccessType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnector">EVChargingConnector</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectorgroup">EVChargingConnectorGroup</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectorreference">EVChargingConnectorReference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingdurationrange">EVChargingDurationRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evcharginglocation">EVChargingLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evcharginglocationfeature">EVChargingLocationFeature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingopeninghours">EVChargingOpeningHours</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingopeninghoursexception">EVChargingOpeningHoursException</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingopeninghoursschedule">EVChargingOpeningHoursSchedule</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingoperator">EVChargingOperator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingpooldetails">EVChargingPoolDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariff">EVChargingTariff</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffdimension">EVChargingTariffDimension</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffelement">EVChargingTariffElement</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffelementcondition">EVChargingTariffElementCondition</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffrequest">EVChargingTariffRequest</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtarifftype">EVChargingTariffType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtruckrestriction">EVChargingTruckRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingvehiclecategory">EVChargingVehicleCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk28EVCP3SearchCompletionHandlera">EVCP3SearchCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evse">Evse</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearchengine">EVSearchEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearcherror">EVSearchError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearchinterface">EVSearchInterface</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearchoptions">EVSearchOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evseconnector">EVSEConnector</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evseinfo">EVSEInfo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsestatus">EVSEStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-facilitytype">FacilityType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fueladditive">FuelAdditive</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fueladditivetype">FuelAdditiveType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fuelstation">FuelStation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fueltype">FuelType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-genericfuel">GenericFuel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoplace">GeoPlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-highlighttype">HighlightType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indexrange">IndexRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-landlinephone">LandlinePhone</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationdetails">LocationDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mobilephone">MobilePhone</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-myplaces">MyPlaces</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offlinesearchengine">OfflineSearchEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offlinesearchindex">OfflineSearchIndex</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-operation">– Operation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-error">– Error</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-options">– Options</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-offlinesearchindexlistener">OfflineSearchIndexListener</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-openinghours">OpeningHours</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-parkingtype">ParkingType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-place">Place</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placecategory">PlaceCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placechain">PlaceChain</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placefilter">PlaceFilter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-ev">– Ev</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placefoodtype">PlaceFoodType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placeidquery">PlaceIdQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placeserializationerror">PlaceSerializationError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placetype">PlaceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-poipaymentdetails">POIPaymentDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-poipaymentmethod">POIPaymentMethod</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-responsedetails">ResponseDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scheduledetails">ScheduleDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searchengine">SearchEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searcherror">SearchError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searchinterface">SearchInterface</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searchoptions">SearchOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-structuredquery">StructuredQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-resulttype">– ResultType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-addresselements">– AddressElements</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-suggestion">Suggestion</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-suggestiontype">SuggestionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-supplierreference">SupplierReference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-textquery">TextQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-area">– Area</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-timeofdayrange">TimeOfDayRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckamenities">TruckAmenities</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckfuel">TruckFuel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webdetails">WebDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webeditorial">WebEditorial</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webimage">WebImage</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webrating">WebRating</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-websiteaddress">WebsiteAddress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-websource">WebSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-w3wsearchengine">W3WSearchEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-w3wsearcherror">W3WSearchError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-w3wsquare">W3WSquare</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-traffic">Traffic</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficengine">TrafficEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficflow">TrafficFlow</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficflowbase">TrafficFlowBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincident">TrafficIncident</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-restrictedvehiclecategory">– RestrictedVehicleCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestriction">– VehicleRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentbase">TrafficIncidentBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentimpact">TrafficIncidentImpact</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentlookupoptions">TrafficIncidentLookupOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentonroute">TrafficIncidentOnRoute</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidenttype">TrafficIncidentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficlocation">TrafficLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficqueryerror">TrafficQueryError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traversability">Traversability</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-trafficradio">TrafficRadio</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficbroadcast">TrafficBroadcast</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficbroadcastparameters">TrafficBroadcastParameters</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tmcdata">TMCData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tmcpreferredsidsrequest">TMCPreferredSidsRequest</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tmcserviceproviderinfo">TMCServiceProviderInfo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tmcservicerequest">TMCServiceRequest</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tmcserviceinterface">TMCServiceInterface</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rdsencryptionkey">RDSEncryptionKey</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rdsencryptionkeysrequest">RDSEncryptionKeysRequest</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-transport">Transport</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busspecifications">BusSpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-carspecifications">CarSpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-hazardousmaterialrestriction">HazardousMaterialRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianspecification">PedestrianSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-restrictiontype">RestrictionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooterspecification">ScooterSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-specificrestriction">SpecificRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxispecification">TaxiSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-timerestriction">TimeRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-category">– Category</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transportmode">TransportMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transportspecification">TransportSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-carbuilder">– CarBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckbuilder">– TruckBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianbuilder">– PedestrianBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooterbuilder">– ScooterBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bicyclebuilder">– BicycleBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxibuilder">– TaxiBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busbuilder">– BusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-privatebusbuilder">– PrivateBusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transporttype">TransportType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckcategory">TruckCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckclass">TruckClass</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckroadtype">TruckRoadType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckfueltype">TruckFuelType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestriction">VehicleRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehicletype">VehicleType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehicleprofile">VehicleProfile</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-weightperaxlegroup">WeightPerAxleGroup</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-venues">Venues</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-crosswalk">Crosswalk</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-classificationstyle">– ClassificationStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-property">Property</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-propertytype">– PropertyType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venue">Venue</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuedelegate">VenueDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuedrawing">VenueDrawing</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueengine">VenueEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venues#/s:7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venues#/s:7heresdk10VenueErrora">VenueError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueerrorcode">VenueErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuegeometry">VenueGeometry</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-internaladdress">– InternalAddress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geometrytype">– GeometryType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lookuptype">– LookupType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuegeometryfiltertype">VenueGeometryFilterType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuegeometrystyle">VenueGeometryStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueinfo">VenueInfo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venues#/s:7heresdk17VenueInfoDataLista">VenueInfoDataList</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuelabelstyle">VenueLabelStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuelevel">VenueLevel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuelifecycledelegate">VenueLifecycleDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venues#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuemap">VenueMap</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuemapdelegate">VenueMapDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuemodel">VenueModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueselectiondelegate">VenueSelectionDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueservice">VenueService</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueoptionalfeature">– VenueOptionalFeature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueservicedelegate">VenueServiceDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venueserviceinitstatus">VenueServiceInitStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuestyle">VenueStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuetopology">VenueTopology</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-accesscharacteristics">– AccessCharacteristics</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-topologydirectionality">– TopologyDirectionality</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-venuetransportmode">VenueTransportMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-key">– Key</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-codingerror">– CodingError</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-warnerengine">WarnerEngine</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-customwarning">CustomWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-customwarningprovider">CustomWarningProvider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-warning">Warning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-warnerengine">WarnerEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-warningdelegate">WarningDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-warningoptions">WarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-warningsregistry">WarningsRegistry</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20classes">Other Classes</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorsectiondetails">IndoorSectionDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationmanager">LocationManager</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20enums">Other Enumerations</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-commercialvehicleroadtype">CommercialVehicleRoadType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-hazardousmaterialtype">HazardousMaterialType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoormaneuveractions">IndoorManeuverActions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-physicalstructure">PhysicalStructure</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehicletypecondition">VehicleTypeCondition</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20functions">Other Functions</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-other20functions#/s:7heresdk24makeIOSPlatformThreadingAA08PlatformD0_pyF">makeIOSPlatformThreading()</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-other20functions#/s:7heresdk12synchronized_7closurexyp_xyXEtlF">synchronized(_:closure:)</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20protocols">Other Protocols</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-matchedlocationlistener">MatchedLocationListener</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20structs">Other Structures</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-admincontextid">AdminContextId</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-administrativecommercialvehiclerules">AdministrativeCommercialVehicleRules</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-driverestregulation">DriveRestRegulation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorlevelchangedata">IndoorLevelChangeData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorrouteplace">IndoorRoutePlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorspacedata">IndoorSpaceData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lanedecreasewarning">LaneDecreaseWarning</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-lanedecreasewarningoptions">LaneDecreaseWarningOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-refreshrouteparameters">RefreshRouteParameters</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadprofilecondition">RoadProfileCondition</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehicleprofilerestriction">VehicleProfileRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestrictioncondition">VehicleRestrictionCondition</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclespecificaccess">VehicleSpecificAccess</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a>
              </li>
            </ul>
          </li>
        </ul>
      </nav>
      <article class="main-content">
        <section>
          <section class="section">
            <h1>LocationSource</h1>
              <div class="declaration">
                <div class="language">
                  
                  <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocationSource</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                </div>
              </div>
            <p>Indicates where the location was computed.</p>

<p>Tells whether the location was calculated on the same device
running HERE SDK or received from an external source.</p>

<p>Example external sources: GNSS modules connected via serial (e.g., u-blox),
or vehicle positioning systems.</p>

<p>Example internal sources: positions computed on the same phone or embedded device
using integrated GNSS or sensor fusion components.</p>

          </section>
          <section class="section task-group-section">
            <div class="task-group">
              <ul>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14LocationSourceO08externalC0yA2CmF"></a>
                    <a name="//apple_ref/swift/Element/externalSource" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14LocationSourceO08externalC0yA2CmF">externalSource</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Location computed outside of the device running HERE SDK.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="k">case</span> <span class="n">externalSource</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14LocationSourceO08internalC0yA2CmF"></a>
                    <a name="//apple_ref/swift/Element/internalSource" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14LocationSourceO08internalC0yA2CmF">internalSource</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Location computed internally on the device running HERE SDK.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="k">case</span> <span class="n">internalSource</span></code></pre>

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
          <p>&copy; 2026 <a class="link" href="" target="_blank" rel="external noopener"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
          <p>Generated by <a class="link" href="https://github.com/realm/jazzy" target="_blank" rel="external noopener">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" target="_blank" rel="external noopener">Realm</a> project.</p>
        </section>
      </article>
    </div>
  </body>
</html>

</div>
`}</HTMLBlock>
