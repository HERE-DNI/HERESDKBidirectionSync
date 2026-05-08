---
title: "Search  Reference"
slug: "sdk-for-ios-navigate-search"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- Search.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Search  Reference</title>
    <link rel="stylesheet" type="text/css" href="css/jazzy.css" />
    <link rel="stylesheet" type="text/css" href="css/highlight.css" />
    <meta charset='utf-8'>
    <script src="js/jquery.min.js" defer></script>
    <script src="js/jazzy.js" defer></script>
    
    <script src="js/lunr.min.js" defer></script>
    <script src="js/typeahead.jquery.js" defer></script>
    <script src="js/jazzy.search.js" defer></script>
  </head>
  <body>
    <a name="//apple_ref/swift/Section/Search" class="dashAnchor"></a>
    <a title="Search  Reference"></a>
    <header>
      <div class="content-wrapper">
        <p><a href="sdk-for-ios-explore-index">heresdk Docs</a> (99% documented)</p>
        <div class="header-right">
          <form role="search" action="search.json">
            <input type="text" placeholder="Search documentation" data-typeahead>
          </form>
        </div>
      </div>
    </header>
    <div class="content-wrapper">
      <p id="breadcrumbs">
        <a href="sdk-for-ios-explore-index">heresdk</a>
        <img id="carat" src="img/carat.png" alt=""/>
        Search  Reference
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
            <h1>Search</h1>
            
          </section>
          <section class="section task-group-section">
            <div class="task-group">
              <ul>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk7AddressV"></a>
                    <a name="//apple_ref/swift/Struct/Address" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk7AddressV">Address</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Information about the address of a location.</p>

<p>Used in <code><a href="sdk-for-ios-explore-place#/s:7heresdk5PlaceC7addressAA7AddressVvp">Place.address</a></code>.</p>

<p>Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
<code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <code><a href="sdk-for-ios-explore-address#/s:7heresdk7AddressV11addressTextSSvp">Address.addressText</a></code>.
Complete address details can be obtained by searching with <code><a href="sdk-for-ios-explore-placeidquery">PlaceIdQuery</a></code>.</p>

                        <a href="sdk-for-ios-explore-address" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Address</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11AddressTypeO"></a>
                    <a name="//apple_ref/swift/Enum/AddressType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11AddressTypeO">AddressType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Address type</p>

                        <a href="sdk-for-ios-explore-addresstype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">AddressType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12AddressQueryV"></a>
                    <a name="//apple_ref/swift/Struct/AddressQuery" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12AddressQueryV">AddressQuery</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify an address query. A <code><a href="sdk-for-ios-explore-addressquery#/s:7heresdk12AddressQueryV5querySSvp">AddressQuery.query</a></code> can consist of parts of an address or full addresses,
optionally comma separated. <code>AddressQuery</code> should only be used to search for parts of the address,
excluding the POI name. For example, &ldquo;Invalidenstraße 116, Berlin, Germany&rdquo; is appropriate, whereas
&ldquo;HERE, Invalidenstraße 116, Berlin, Germany&rdquo; is not. To be able to include the POI name, use
<code><a href="sdk-for-ios-explore-textquery">TextQuery</a></code> instead. <code><a href="sdk-for-ios-explore-searchoptions#/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp">SearchOptions.languageCode</a></code> specifies the language of the
<code><a href="sdk-for-ios-explore-addressquery#/s:7heresdk12AddressQueryV5querySSvp">AddressQuery.query</a></code> and determines the preferred language of the results.</p>

                        <a href="sdk-for-ios-explore-addressquery" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AddressQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8AreaTypeO"></a>
                    <a name="//apple_ref/swift/Enum/AreaType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8AreaTypeO">AreaType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a type of area like country, state, city, county, etc.</p>

                        <a href="sdk-for-ios-explore-areatype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">AreaType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15BusinessDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/BusinessDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15BusinessDetailsV">BusinessDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains place details such as contacts, opening hours and some electro vehicle info.</p>

                        <a href="sdk-for-ios-explore-businessdetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BusinessDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13CategoryQueryV"></a>
                    <a name="//apple_ref/swift/Struct/CategoryQuery" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13CategoryQueryV">CategoryQuery</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify a query by categories.</p>

                        <a href="sdk-for-ios-explore-categoryquery" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CategoryQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk7ContactV"></a>
                    <a name="//apple_ref/swift/Struct/Contact" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk7ContactV">Contact</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents contact information.</p>

                        <a href="sdk-for-ios-explore-contact" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Contact</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9DateRangeV"></a>
                    <a name="//apple_ref/swift/Struct/DateRange" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9DateRangeV">DateRange</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the date range when the tariff element is valid. This is typically used to indicate
seasonal tariffs or to announce an update to the tariff in advance. It may also be used to
indicate spot prices, together with time period.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-daterange" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DateRange</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9DayOfWeekO"></a>
                    <a name="//apple_ref/swift/Enum/DayOfWeek" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9DayOfWeekO">DayOfWeek</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the day of the week.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-dayofweek" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">DayOfWeek</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk7DetailsV"></a>
                    <a name="//apple_ref/swift/Struct/Details" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk7DetailsV">Details</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains details of a specific place, such as contact information,
opening hours and assigned categories.</p>

                        <a href="sdk-for-ios-explore-details" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Details</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12EmailAddressV"></a>
                    <a name="//apple_ref/swift/Struct/EmailAddress" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12EmailAddressV">EmailAddress</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents data related to specific email address.</p>

                        <a href="sdk-for-ios-explore-emailaddress" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EmailAddress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk24EMobilityServiceProviderV"></a>
                    <a name="//apple_ref/swift/Struct/EMobilityServiceProvider" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk24EMobilityServiceProviderV">EMobilityServiceProvider</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>eMSP (e-Mobility Service Provider) for which the EV station operator has EV roaming agreements.
It is only available for online search.</p>

                        <a href="sdk-for-ios-explore-emobilityserviceprovider" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EMobilityServiceProvider</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9EnergyMixV"></a>
                    <a name="//apple_ref/swift/Struct/EnergyMix" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9EnergyMixV">EnergyMix</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents details on the energy supplied at the charging location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-energymix" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EnergyMix</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12EnergySourceV"></a>
                    <a name="//apple_ref/swift/Struct/EnergySource" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12EnergySourceV">EnergySource</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Energy source of EV charging point.
EnergyMix contains a list of this representing the energy sources.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-energysource" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EnergySource</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16EnergySourceTypeO"></a>
                    <a name="//apple_ref/swift/Enum/EnergySourceType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16EnergySourceTypeO">EnergySourceType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents energy source type.
EnergySource contains this representing the type of the energy source.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-energysourcetype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EnergySourceType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19EnvironmentalImpactV"></a>
                    <a name="//apple_ref/swift/Struct/EnvironmentalImpact" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19EnvironmentalImpactV">EnvironmentalImpact</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents environmental impact for an environmental impact category.
EnergyMix contains an list of this representing the environmental impacts of different categories.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-environmentalimpact" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EnvironmentalImpact</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk27EnvironmentalImpactCategoryO"></a>
                    <a name="//apple_ref/swift/Enum/EnvironmentalImpactCategory" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk27EnvironmentalImpactCategoryO">EnvironmentalImpactCategory</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents environmental impacts category of the environmental impact for energy mix.
EnvironmentalImpact contains this representing the category of the environmental impact.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-environmentalimpactcategory" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EnvironmentalImpactCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk25EVAccessRestrictionReasonO"></a>
                    <a name="//apple_ref/swift/Enum/EVAccessRestrictionReason" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk25EVAccessRestrictionReasonO">EVAccessRestrictionReason</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the restriction reason of an <code><a href="sdk-for-ios-explore-evchargingpool">EVChargingPool</a></code>.</p>

                        <a href="sdk-for-ios-explore-evaccessrestrictionreason" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVAccessRestrictionReason</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12EVAccessTypeO"></a>
                    <a name="//apple_ref/swift/Enum/EVAccessType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12EVAccessTypeO">EVAccessType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the accessibility level of an <code><a href="sdk-for-ios-explore-evchargingpool">EVChargingPool</a></code>.</p>

                        <a href="sdk-for-ios-explore-evaccesstype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVAccessType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19EVChargingConnectorV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingConnector" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19EVChargingConnectorV">EVChargingConnector</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a connector at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingconnector" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingConnector</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk24EVChargingConnectorGroupV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingConnectorGroup" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV">EVChargingConnectorGroup</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the connector group at the charging location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingconnectorgroup" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingConnectorGroup</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk28EVChargingConnectorReferenceV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingConnectorReference" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk28EVChargingConnectorReferenceV">EVChargingConnectorReference</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a pairing of an EVSE and its connector(s) that belong to a group.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingconnectorreference" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingConnectorReference</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23EVChargingDurationRangeV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingDurationRange" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23EVChargingDurationRangeV">EVChargingDurationRange</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Duration of the charging session when the tariff element is valid, in seconds.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingdurationrange" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingDurationRange</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk18EVChargingLocationC"></a>
                    <a name="//apple_ref/swift/Class/EVChargingLocation" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk18EVChargingLocationC">EVChargingLocation</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>An electric vehicle (EV) charging location.</p>

<p>The semantics generally follow the OCPI 2.2.1 standard.</p>

<p>Known EV-specific acronyms:</p>

<ul>
<li>EV: Electric Vehicle</li>
<li>OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, <a href="https://evroaming.org/">https://evroaming.org/</a>)</li>
<li>CPO: Charge Point Operator (company that runs the EV charging location)</li>
<li>eMSP: e-Mobility Service Provider (customer-facing company)</li>
<li>EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)</li>
</ul>

<p>A charging location includes a collection of one or more EV supply equipment (EVSE) instances.
Typically, the charging location is the exact location of the group of EVSEs,
simplified to a single point, but it can also be the entrance of a parking structure
which contains these EVSEs.
Each EVSE supports more precise position, where applicable.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evcharginglocation" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">EVChargingLocation</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">EVChargingLocation</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">EVChargingLocation</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk25EVChargingLocationFeatureO"></a>
                    <a name="//apple_ref/swift/Enum/EVChargingLocationFeature" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO">EVChargingLocationFeature</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Optional features that can be requested for EV charging locations.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evcharginglocationfeature" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVChargingLocationFeature</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk22EVChargingOpeningHoursV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingOpeningHours" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV">EVChargingOpeningHours</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the times when the EVSEs at the charging location can be accessed for charging.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingopeninghours" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingOpeningHours</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk31EVChargingOpeningHoursExceptionV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingOpeningHoursException" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk31EVChargingOpeningHoursExceptionV">EVChargingOpeningHoursException</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents exceptions to the regular opening hours schedule for EV charging locations,
such as special closures or extended hours.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingopeninghoursexception" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingOpeningHoursException</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk30EVChargingOpeningHoursScheduleV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingOpeningHoursSchedule" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk30EVChargingOpeningHoursScheduleV">EVChargingOpeningHoursSchedule</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Opening hours schedule for EV charging locations, represented by a list of days of the week
during which the location is open in the given time periods.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingopeninghoursschedule" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingOpeningHoursSchedule</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk18EVChargingOperatorV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingOperator" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk18EVChargingOperatorV">EVChargingOperator</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents name and optionally other details about operator, suboperator, or e-Mobility service provider.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingoperator" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingOperator</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk21EVChargingPoolDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingPoolDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV">EVChargingPoolDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Electric vehicle charging pool details.</p>

                        <a href="sdk-for-ios-explore-evchargingpooldetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingPoolDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16EVChargingTariffV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingTariff" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16EVChargingTariffV">EVChargingTariff</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Tariffs provide detailed pricing information for charging electric vehicles at a specific location.
Each tariff describes how costs are calculated based on various factors such as energy consumed,
time spent charging, and session duration.
Tariffs are typically associated with specific connectors or connector groups, and are only
included in the response when relevant data is available and requested.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtariff" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTariff</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk25EVChargingTariffDimensionO"></a>
                    <a name="//apple_ref/swift/Enum/EVChargingTariffDimension" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk25EVChargingTariffDimensionO">EVChargingTariffDimension</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the dimension the price component, which determines what is being charged and how:</p>

<ul>
<li>time: Price per unit of time spent charging.</li>
<li>energy: Price per unit of energy consumed during charging.</li>
<li>flat: One-time fee charged per session.</li>
<li>parking time: Price per unit of time not charging but parked at the charger.</li>
</ul>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtariffdimension" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVChargingTariffDimension</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23EVChargingTariffElementV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingTariffElement" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23EVChargingTariffElementV">EVChargingTariffElement</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a tariff element, which defines how pricing is applied.
The associated condition assists the client in selecting the appropriate element for a charging session.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtariffelement" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTariffElement</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk32EVChargingTariffElementConditionV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingTariffElementCondition" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV">EVChargingTariffElementCondition</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Condition that the charging session needs to meet to apply the tariff element.
Tariff elements may include conditions that define when they apply:</p>

<ul>
<li>Time of day (e.g., 22:00–06:00)</li>
<li>Day of week (e.g., weekends only)</li>
</ul><div class="aside aside-date">
    <p class="aside-title">Date</p>
    Date range (e.g., seasonal pricing)

</div><ul>
<li>Charging session duration</li>
<li>Battery level thresholds (e.g., overstay fees)</li>
</ul>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtariffelementcondition" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTariffElementCondition</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk30EVChargingTariffPriceComponentV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingTariffPriceComponent" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk30EVChargingTariffPriceComponentV">EVChargingTariffPriceComponent</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the price component of an EV charging tariff.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtariffpricecomponent" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTariffPriceComponent</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23EVChargingTariffRequestV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingTariffRequest" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23EVChargingTariffRequestV">EVChargingTariffRequest</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a search option to choose the eMSP or CPO whose tariff should be included in the response.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtariffrequest" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTariffRequest</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk20EVChargingTariffTypeO"></a>
                    <a name="//apple_ref/swift/Enum/EVChargingTariffType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk20EVChargingTariffTypeO">EVChargingTariffType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the tariff pricing model (adhoc, emsp, or cpo).
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtarifftype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVChargingTariffType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk26EVChargingTruckRestrictionV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingTruckRestriction" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk26EVChargingTruckRestrictionV">EVChargingTruckRestriction</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents access restrictions for trucks and light commercial vehicles.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingtruckrestriction" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTruckRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk25EVChargingVehicleCategoryO"></a>
                    <a name="//apple_ref/swift/Enum/EVChargingVehicleCategory" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk25EVChargingVehicleCategoryO">EVChargingVehicleCategory</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents the category of the vehicle supported at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evchargingvehiclecategory" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVChargingVehicleCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk28EVCP3SearchCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/EVCP3SearchCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk28EVCP3SearchCompletionHandlera">EVCP3SearchCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method that will be called on the main thread when a search operation in <code><a href="sdk-for-ios-explore-evsearchengine">EVSearchEngine</a></code>
has been completed.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">EVCP3SearchCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-evsearcherror">EVSearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">chargingLocations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-evcharginglocation">EVChargingLocation</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>error</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The ev search error.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>chargingLocations</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The ev charging locations.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk4EvseV"></a>
                    <a name="//apple_ref/swift/Struct/Evse" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk4EvseV">Evse</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.</p>

                        <a href="sdk-for-ios-explore-evse" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Evse</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14EVSearchEngineC"></a>
                    <a name="//apple_ref/swift/Class/EVSearchEngine" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14EVSearchEngineC">EVSearchEngine</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The <code>EVSearchEngine</code> API provides detailed information about charging locations.
It requires an online connection to execute the requests.
A licence is required to use this API. Details can be found in
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-v3-developer-guide/page/topics/quick-start-platform.html">HERE EV Charge Points API v3 - Developer Guide</a>.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evsearchengine" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">EVSearchEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-evsearchinterface">EVSearchInterface</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">EVSearchEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">EVSearchEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13EVSearchErrorO"></a>
                    <a name="//apple_ref/swift/Enum/EVSearchError" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13EVSearchErrorO">EVSearchError</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies possible errors that <code><a href="sdk-for-ios-explore-evsearchengine">EVSearchEngine</a></code> may report.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evsearcherror" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVSearchError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17EVSearchInterfaceP"></a>
                    <a name="//apple_ref/swift/Protocol/EVSearchInterface" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17EVSearchInterfaceP">EVSearchInterface</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Provides the protocol for the <code><a href="sdk-for-ios-explore-evsearchengine">EVSearchEngine</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evsearchinterface" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">EVSearchInterface</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15EVSearchOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/EVSearchOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15EVSearchOptionsV">EVSearchOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Encapsulates additional options that control the behavior of <code><a href="sdk-for-ios-explore-evsearchengine">EVSearchEngine</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evsearchoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVSearchOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13EVSEConnectorV"></a>
                    <a name="//apple_ref/swift/Struct/EVSEConnector" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13EVSEConnectorV">EVSEConnector</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>EVSE connector.</p>

                        <a href="sdk-for-ios-explore-evseconnector" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVSEConnector</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8EVSEInfoV"></a>
                    <a name="//apple_ref/swift/Struct/EVSEInfo" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8EVSEInfoV">EVSEInfo</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents an EVSE at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-evseinfo" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVSEInfo</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10EVSEStatusO"></a>
                    <a name="//apple_ref/swift/Enum/EVSEStatus" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10EVSEStatusO">EVSEStatus</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>EVSE status</p>

                        <a href="sdk-for-ios-explore-evsestatus" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVSEStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12FacilityTypeO"></a>
                    <a name="//apple_ref/swift/Enum/FacilityType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12FacilityTypeO">FacilityType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents facility type available at the location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-facilitytype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FacilityType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12FuelAdditiveV"></a>
                    <a name="//apple_ref/swift/Struct/FuelAdditive" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12FuelAdditiveV">FuelAdditive</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains fuel additive information for generic fuel type.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-fueladditive" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FuelAdditive</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16FuelAdditiveTypeO"></a>
                    <a name="//apple_ref/swift/Enum/FuelAdditiveType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16FuelAdditiveTypeO">FuelAdditiveType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Defines possible fuel additives that a fuel could contain.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-fueladditivetype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FuelAdditiveType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11FuelStationV"></a>
                    <a name="//apple_ref/swift/Struct/FuelStation" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11FuelStationV">FuelStation</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains information about a specific fuel station.</p>

<p>Use <code><a href="sdk-for-ios-explore-placecategory#/s:7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ">PlaceCategory.businessAndServicesPetrolGasolineStation</a></code> to find fuel stations.
In the <code><a href="sdk-for-ios-explore-details">Details</a></code> of a <code><a href="sdk-for-ios-explore-place">Place</a></code> result you can find the associated fuel station information,
if any.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-fuelstation" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FuelStation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8FuelTypeO"></a>
                    <a name="//apple_ref/swift/Enum/FuelType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8FuelTypeO">FuelType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Defines possible fuel types provided by a fuel station.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-fueltype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FuelType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11GenericFuelV"></a>
                    <a name="//apple_ref/swift/Struct/GenericFuel" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11GenericFuelV">GenericFuel</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains generic fuel type info of fuel station.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-genericfuel" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GenericFuel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8GeoPlaceV"></a>
                    <a name="//apple_ref/swift/Struct/GeoPlace" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8GeoPlaceV">GeoPlace</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>GeoPlace struct represents a location object:
such as a country, a city, a point of interest (POI) etc.
It can be used for PersonalPlace creation, in order to provide search on custom places.</p>

                        <a href="sdk-for-ios-explore-geoplace" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeoPlace</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13HighlightTypeO"></a>
                    <a name="//apple_ref/swift/Enum/HighlightType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13HighlightTypeO">HighlightType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies members of Suggestion class to which input query can be matched.</p>

                        <a href="sdk-for-ios-explore-highlighttype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">HighlightType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10IndexRangeC"></a>
                    <a name="//apple_ref/swift/Class/IndexRange" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10IndexRangeC">IndexRange</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Holds information to which part of the text, input query was matched.
The first character is denoted by a value of 0.</p>

                        <a href="sdk-for-ios-explore-indexrange" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IndexRange</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndexRange</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndexRange</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13LandlinePhoneV"></a>
                    <a name="//apple_ref/swift/Struct/LandlinePhone" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13LandlinePhoneV">LandlinePhone</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents data related to specific landline phone number.</p>

                        <a href="sdk-for-ios-explore-landlinephone" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LandlinePhone</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15LocationDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/LocationDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15LocationDetailsV">LocationDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains geographical info about location</p>

                        <a href="sdk-for-ios-explore-locationdetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LocationDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11MobilePhoneV"></a>
                    <a name="//apple_ref/swift/Struct/MobilePhone" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11MobilePhoneV">MobilePhone</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents data related to specific mobile phone number.</p>

                        <a href="sdk-for-ios-explore-mobilephone" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MobilePhone</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8MyPlacesC"></a>
                    <a name="//apple_ref/swift/Class/MyPlaces" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8MyPlacesC">MyPlaces</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Provides means to populate personal places data source. Also acts as a
owner of the collection of personal places. MyPlaces is
memory-only object: nothing is persisted and/or sent over the network.
Client has full control on how to store personal places.</p>

                        <a href="sdk-for-ios-explore-myplaces" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MyPlaces</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MyPlaces</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MyPlaces</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19OfflineSearchEngineC"></a>
                    <a name="//apple_ref/swift/Class/OfflineSearchEngine" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19OfflineSearchEngineC">OfflineSearchEngine</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The OfflineSearchEngine works without internet and unlocks the search and geocoding
capabilities of HERE services to provide developers with unmatched flexibility
to create differentiating location-enabled applications.</p>

<p>It provides the same interfaces as the SearchEngine, but the results may slightly
differ as the results are taken from already downloaded map data instead of initiating
a new request to a HERE backend service. This way the data may be, for example, older
compared to the data you may receive when using the SearchEngine. On the other hand,
this class provides results faster as no online connection is necessary.</p>

<p>In comparison to the SearchEngine, there are a few limitations:</p>

<ul>
<li>The IDs of POIs are different and may differ among different map versions.</li>
<li>The implementation is different and the resources are limited, so the results can differ.</li>
<li>OfflineSearchEngine sometimes doesn&rsquo;t return the requested number of results.</li>
</ul>

<p>Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data.
However, cached data may be incomplete, which can result in searches returning partial or incomplete information.
Therefore, it is recommended to use persistent map data.
Make sure that at least <code><a href="sdk-for-ios-explore-feature#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">LayerConfiguration.Feature.offlineSearch</a></code> is enabled.
For EV rich attributes also enable <code><a href="sdk-for-ios-explore-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>,
for truck rich attributes also enable <code><a href="sdk-for-ios-explore-feature#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">LayerConfiguration.Feature.truckServiceAttributes</a></code>,
for fuel station rich attributes also enable <code><a href="sdk-for-ios-explore-feature#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">LayerConfiguration.Feature.fuelStationAttributes</a></code>
in <code><a href="sdk-for-ios-explore-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>

                        <a href="sdk-for-ios-explore-offlinesearchengine" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">OfflineSearchEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searchinterface">SearchInterface</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineSearchEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineSearchEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk18OfflineSearchIndexC"></a>
                    <a name="//apple_ref/swift/Class/OfflineSearchIndex" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk18OfflineSearchIndexC">OfflineSearchIndex</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-offlinesearchindex" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">OfflineSearchIndex</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineSearchIndex</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineSearchIndex</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk26OfflineSearchIndexListenerP"></a>
                    <a name="//apple_ref/swift/Protocol/OfflineSearchIndexListener" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk26OfflineSearchIndexListenerP">OfflineSearchIndexListener</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Protocol to get updates about progress
of creating persistent map index.</p>

<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-offlinesearchindexlistener" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">OfflineSearchIndexListener</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12OpeningHoursV"></a>
                    <a name="//apple_ref/swift/Struct/OpeningHours" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12OpeningHoursV">OpeningHours</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents opening hours information.</p>

                        <a href="sdk-for-ios-explore-openinghours" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">OpeningHours</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11ParkingTypeO"></a>
                    <a name="//apple_ref/swift/Enum/ParkingType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11ParkingTypeO">ParkingType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents parking type available at the location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-parkingtype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ParkingType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk5PlaceC"></a>
                    <a name="//apple_ref/swift/Class/Place" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk5PlaceC">Place</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a location object, such as a country, a city, a point of interest (POI) etc.</p>

                        <a href="sdk-for-ios-explore-place" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Place</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Place</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Place</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13PlaceCategoryC"></a>
                    <a name="//apple_ref/swift/Class/PlaceCategory" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13PlaceCategoryC">PlaceCategory</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a category of place with different levels of granularity.
This class also defines a set of most commonly used categories.</p>

                        <a href="sdk-for-ios-explore-placecategory" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PlaceCategory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PlaceCategory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PlaceCategory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10PlaceChainV"></a>
                    <a name="//apple_ref/swift/Struct/PlaceChain" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10PlaceChainV">PlaceChain</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Parameters related to HERE Places chain system.</p>

                        <a href="sdk-for-ios-explore-placechain" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PlaceChain</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11PlaceFilterV"></a>
                    <a name="//apple_ref/swift/Struct/PlaceFilter" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11PlaceFilterV">PlaceFilter</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The filter options to specify a place.
Consists of fuel, truck and EV options.</p>

                        <a href="sdk-for-ios-explore-placefilter" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PlaceFilter</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13PlaceFoodTypeV"></a>
                    <a name="//apple_ref/swift/Struct/PlaceFoodType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13PlaceFoodTypeV">PlaceFoodType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Parameters related to HERE Places cuisine system.</p>

                        <a href="sdk-for-ios-explore-placefoodtype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PlaceFoodType</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12PlaceIdQueryV"></a>
                    <a name="//apple_ref/swift/Struct/PlaceIdQuery" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12PlaceIdQueryV">PlaceIdQuery</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify a Place id query.</p>

                        <a href="sdk-for-ios-explore-placeidquery" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PlaceIdQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk30PlaceIdSearchCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/PlaceIdSearchCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method will be called on the main thread when a search by id call has been completed.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">PlaceIdSearchCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">searchError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searcherror">SearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">place</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-place">Place</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>searchError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The search error.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>place</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The place.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/PlaceIdSearchExtendedCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method will be called on the main thread when a search by id call has been completed.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">PlaceIdSearchExtendedCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">searchError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searcherror">SearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">place</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-place">Place</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">responseDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-responsedetails">ResponseDetails</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>searchError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The search error.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>place</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The place.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>responseDetails</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The response details.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23PlaceSerializationErrorO"></a>
                    <a name="//apple_ref/swift/Enum/PlaceSerializationError" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23PlaceSerializationErrorO">PlaceSerializationError</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents and error, which occurs during place serialization and deserialization routines.</p>

                        <a href="sdk-for-ios-explore-placeserializationerror" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PlaceSerializationError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PlaceSerializationError</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk27PlaceSerializationExceptiona"></a>
                    <a name="//apple_ref/swift/Alias/PlaceSerializationException" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Place serialization exception</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">PlaceSerializationException</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-placeserializationerror">PlaceSerializationError</a></span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9PlaceTypeO"></a>
                    <a name="//apple_ref/swift/Enum/PlaceType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9PlaceTypeO">PlaceType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies place type of Place result from a search query.</p>

                        <a href="sdk-for-ios-explore-placetype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PlaceType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17POIPaymentDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/POIPaymentDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17POIPaymentDetailsV">POIPaymentDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Details about the payment options at the POI.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-poipaymentdetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">POIPaymentDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16POIPaymentMethodV"></a>
                    <a name="//apple_ref/swift/Struct/POIPaymentMethod" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16POIPaymentMethodV">POIPaymentMethod</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Holds constants that represent payment methods.</p>

<p>See <code><a href="sdk-for-ios-explore-poipaymentdetails">POIPaymentDetails</a></code> for usage.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-poipaymentmethod" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">POIPaymentMethod</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15ResponseDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/ResponseDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15ResponseDetailsV">ResponseDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Structure holding various information received with response to a query.</p>

                        <a href="sdk-for-ios-explore-responsedetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ResponseDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15ScheduleDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/ScheduleDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15ScheduleDetailsV">ScheduleDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Encapsulates schedule details complying with the iCalendar specification: <a href="https://tools.ietf.org/html/rfc5545">https://tools.ietf.org/html/rfc5545</a>.</p>

                        <a href="sdk-for-ios-explore-scheduledetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ScheduleDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23SearchCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/SearchCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method will be called on the main thread when a search call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">SearchCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">searchError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searcherror">SearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">places</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-place">Place</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>searchError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>places</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The list of search results. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk31SearchExtendedCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/SearchExtendedCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method will be called on the main thread when a search call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">SearchExtendedCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">searchError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searcherror">SearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">places</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-place">Place</a></span><span class="p">]?,</span> <span class="n">_</span> <span class="nv">responseDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-responsedetails">ResponseDetails</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>searchError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>places</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The list of search results. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>responseDetails</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>Additional information provided with response. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12SearchEngineC"></a>
                    <a name="//apple_ref/swift/Class/SearchEngine" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12SearchEngineC">SearchEngine</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services
to provide developers with unmatched flexibility to create differentiating location-enabled
applications. It enables to search for HERE points of interests, forward and reverse
geocode addresses and geographic coordinates from the HERE map and search for suggested addresses
or place candidates based on incomplete or misspelled queries.</p>

<p>It also allows to search along a given <code><a href="sdk-for-ios-explore-geopolyline">GeoPolyline</a></code> set inside a <code><a href="sdk-for-ios-explore-geocorridor">GeoCorridor</a></code>
as part of a <code><a href="sdk-for-ios-explore-textquery">TextQuery</a></code>.</p>

<p>The SearchEngine API requires an online connection to execute the requests.</p>

<p><strong>Note:</strong> All methods are provided in two flavors. One uses a <code><a href="sdk-for-ios-explore-search#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></code> and the
other uses a <code><a href="sdk-for-ios-explore-search#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></code>: The later adds a <code><a href="sdk-for-ios-explore-responsedetails">ResponseDetails</a></code> result type
that provides the <code>requestId</code> of a search request and a <code>correlationId</code> to identify multiple,
related queries. This may be useful for debug purposes.</p>

                        <a href="sdk-for-ios-explore-searchengine" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SearchEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searchinterface">SearchInterface</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SearchEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SearchEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11SearchErrorO"></a>
                    <a name="//apple_ref/swift/Enum/SearchError" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11SearchErrorO">SearchError</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies possible errors that may result from a search query.</p>

                        <a href="sdk-for-ios-explore-searcherror" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SearchError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15SearchInterfaceP"></a>
                    <a name="//apple_ref/swift/Protocol/SearchInterface" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15SearchInterfaceP">SearchInterface</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Provides the protocol for the online and offline
search engines.</p>

                        <a href="sdk-for-ios-explore-searchinterface" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">SearchInterface</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13SearchOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/SearchOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13SearchOptionsV">SearchOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Encapsulates options that control the behavior of search and suggest operations.</p>

                        <a href="sdk-for-ios-explore-searchoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SearchOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15StructuredQueryV"></a>
                    <a name="//apple_ref/swift/Struct/StructuredQuery" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15StructuredQueryV">StructuredQuery</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify a structured query.
Only supported in <code><a href="sdk-for-ios-explore-offlinesearchengine">OfflineSearchEngine</a></code> (only available for the Navigate license).</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-structuredquery" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">StructuredQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10SuggestionC"></a>
                    <a name="//apple_ref/swift/Class/Suggestion" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10SuggestionC">Suggestion</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Suggestion is meant to provide relevant suggestions to partial queries, like &ldquo;restaur&rdquo;, &ldquo;starbu&rdquo;, &ldquo;eiffel&rdquo;.
Represents a relevant response to user queries.
Suggestions (please check <code><a href="sdk-for-ios-explore-suggestiontype">SuggestionType</a></code>) are either:
Place: <code><a href="sdk-for-ios-explore-suggestiontype#/s:7heresdk14SuggestionTypeO5placeyA2CmF">SuggestionType.place</a></code>
Query: <code><a href="sdk-for-ios-explore-suggestiontype#/s:7heresdk14SuggestionTypeO5chainyA2CmF">SuggestionType.chain</a></code> or <code><a href="sdk-for-ios-explore-suggestiontype#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">SuggestionType.category</a></code></p>

<p>With &ldquo;Place&rdquo; you get data for a concrete place in the world.
With &ldquo;Query&rdquo; something to follow-up, a way to perform more focused search.</p>

                        <a href="sdk-for-ios-explore-suggestion" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Suggestion</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Suggestion</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Suggestion</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14SuggestionTypeO"></a>
                    <a name="//apple_ref/swift/Enum/SuggestionType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14SuggestionTypeO">SuggestionType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies the type of suggestion returned for query.</p>

                        <a href="sdk-for-ios-explore-suggestiontype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SuggestionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk24SuggestCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/SuggestCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method will be called on the main thread when a suggest call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">SuggestCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">searchError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searcherror">SearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">suggestions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-suggestion">Suggestion</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>searchError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>suggestions</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The list of suggestion results. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk32SuggestExtendedCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/SuggestExtendedCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method will be called on the main thread when a suggest call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.
This API is not supported by offline search.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">SuggestExtendedCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">searchError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-searcherror">SearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">suggestions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-suggestion">Suggestion</a></span><span class="p">]?,</span> <span class="n">_</span> <span class="nv">responseDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-responsedetails">ResponseDetails</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>searchError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>suggestions</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The list of suggestion results. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>responseDetails</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>Additional information provided with response. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17SupplierReferenceV"></a>
                    <a name="//apple_ref/swift/Struct/SupplierReference" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17SupplierReferenceV">SupplierReference</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifier of the place as provided by the supplier</p>

                        <a href="sdk-for-ios-explore-supplierreference" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SupplierReference</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9TextQueryV"></a>
                    <a name="//apple_ref/swift/Struct/TextQuery" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9TextQueryV">TextQuery</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify a text query.</p>

                        <a href="sdk-for-ios-explore-textquery" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TextQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14TimeOfDayRangeV"></a>
                    <a name="//apple_ref/swift/Struct/TimeOfDayRange" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14TimeOfDayRangeV">TimeOfDayRange</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Time period when the tariff element is valid, in local time. The time period wraps around to
the next day, when end time of the period <code><a href="sdk-for-ios-explore-timeofdayrange#/s:7heresdk14TimeOfDayRangeV2toSSvp">TimeOfDayRange.to</a></code>
is smaller than the beginning <code><a href="sdk-for-ios-explore-timeofdayrange#/s:7heresdk14TimeOfDayRangeV4fromSSvp">TimeOfDayRange.from</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-timeofdayrange" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TimeOfDayRange</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14TruckAmenitiesV"></a>
                    <a name="//apple_ref/swift/Struct/TruckAmenities" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14TruckAmenitiesV">TruckAmenities</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Truck amenities struct, represents availability (true/false) for each feature,
except shower_count - number of showers, if data is available.
Note: This is a BETA feature and thus subject to change.</p>

                        <a href="sdk-for-ios-explore-truckamenities" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckAmenities</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9TruckFuelV"></a>
                    <a name="//apple_ref/swift/Struct/TruckFuel" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9TruckFuelV">TruckFuel</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains truck fuel type info of fuel station.
Note: This is a BETA feature and thus subject to change.</p>

                        <a href="sdk-for-ios-explore-truckfuel" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckFuel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10WebDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/WebDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10WebDetailsV">WebDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains information about images, editorials, rating and a urls to them.</p>

                        <a href="sdk-for-ios-explore-webdetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WebDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12WebEditorialV"></a>
                    <a name="//apple_ref/swift/Struct/WebEditorial" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12WebEditorialV">WebEditorial</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains information about editorial article and a link to it.</p>

                        <a href="sdk-for-ios-explore-webeditorial" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WebEditorial</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8WebImageV"></a>
                    <a name="//apple_ref/swift/Struct/WebImage" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8WebImageV">WebImage</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains image information and direct link to it.</p>

                        <a href="sdk-for-ios-explore-webimage" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WebImage</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9WebRatingV"></a>
                    <a name="//apple_ref/swift/Struct/WebRating" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9WebRatingV">WebRating</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains information about rating and a url to review.</p>

                        <a href="sdk-for-ios-explore-webrating" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WebRating</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14WebsiteAddressV"></a>
                    <a name="//apple_ref/swift/Struct/WebsiteAddress" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14WebsiteAddressV">WebsiteAddress</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents data related to specific website address</p>

                        <a href="sdk-for-ios-explore-websiteaddress" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WebsiteAddress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9WebSourceV"></a>
                    <a name="//apple_ref/swift/Struct/WebSource" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9WebSourceV">WebSource</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains information about provider of the item
and a direct link to the item.</p>

                        <a href="sdk-for-ios-explore-websource" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WebSource</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15W3WSearchEngineC"></a>
                    <a name="//apple_ref/swift/Class/W3WSearchEngine" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15W3WSearchEngineC">W3WSearchEngine</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>what3words is an alternative geocode system designed to identify any location on the planet.
The system divides the world into a grid of 57 trillion 3-by-3-metre squares, each of which
has a three-word address. For example, the front door of HERE’s Berlin office is identified by
&ldquo;///wage.mere.heap&rdquo;.
<code>W3WSearchEngine</code> allows you to convert 3 word addresses to coordinates and also coordinates
to 3 word addresses.</p>

<p><strong>Note:</strong> Using W3WSearchEngine requires a licence to access HERE what3words APIs.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-w3wsearchengine" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">W3WSearchEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">W3WSearchEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">W3WSearchEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14W3WSearchErrorO"></a>
                    <a name="//apple_ref/swift/Enum/W3WSearchError" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14W3WSearchErrorO">W3WSearchError</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies possible errors that may result from a w3w search query.</p>

                        <a href="sdk-for-ios-explore-w3wsearcherror" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">W3WSearchError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9W3WSquareV"></a>
                    <a name="//apple_ref/swift/Struct/W3WSquare" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9W3WSquareV">W3WSquare</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains information about one of the squares in the what3words geocode system.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-w3wsquare" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">W3WSquare</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk26W3WSearchCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/W3WSearchCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The method that will be called on the main thread when a search operation in <code><a href="sdk-for-ios-explore-w3wsearchengine">W3WSearchEngine</a></code>
has been completed.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">W3WSearchCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">searchError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-w3wsearcherror">W3WSearchError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">square</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-w3wsquare">W3WSquare</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>searchError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The w3w search error.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>square</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The w3w square.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
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
