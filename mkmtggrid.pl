#!/usr/bin/env perl

#use strict;

# 2016
# @users = ('ono', 'y-sato', 'mashita', 'miyake', 'kawamura', 'shindo', 'anjyu', 'fujii', 'furuhasi', 'tajimi', 'noda', 'hayakawa', 'matuyama');
# 2017
#@users = ('kawamura', 'shindo', 'anjyu', 'fujii', 'furuhasi', 'tajimi', 'hayakawa', 'matuyama', 'iida', 'inouchi', 'hayashi', 'futamase');

# 2018
# @users = ('tajimi', 'hayakawa', 'matuyama', 'iida', 'inouchi', 'hayashi', 'futamase', 'kawaguti', 'kobayasi', 'takaoka', 'takeishi');
# 2019
# @users = ('iida', 'inouchi', 'futamase', 'kawaguti', 'kobayasi', 'takaoka', 'takeishi', 'y-asai', 'kuroda', 'yamasita');
#2020
@users = ('kawaguti', 'kobayasi', 'takaoka', 'takeishi', 'y-asai', 'kuroda', 'yamasita', 'okuda', 'nakahara', 'k_yamamoto');

sub outrow {
  my( $DATESTR ) = @_;
  $DATESTR =~ /([0-9]{4})([0-9]{2})([0-9]{2})/;
  my( $y, $m, $d ) = ($1, $2, $3);
  print "|| ${m}/${d} ||";
  foreach( @users ){
    print " [[attachment:${_}-camp-${y}${m}${d}.pptx|title]] ||";
  }
  print "\n";
}


# main

if( $ARGV[0] =~ /^[0-9]{8}$/ ){
    &outrow( $ARGV[0] );
    exit 0;
}elsif( "z" . $ARGV[0] eq "z" ){
    my($z,$z,$z,$md,$m,$y,$z,$z,$z) = localtime(time);
    $y+=1900; $m+=1;
    &outrow( sprintf("%04d%02d%02d", $y, $m, $md ) );
    exit 0;
}else{
    my($TARGETDIR) = '.';
    if( -d $ARGV[0] ){
        $TARGETDIR = $ARGV[0];
    }
    opendir(D, ${TARGETDIR});
    @FILES = grep(/\.pptx$/, readdir(D));
    @DATES = ();
    foreach( @FILES ){
	/^.+-camp-([0-9]{8})\.ppt[x]$/;
	push(@DATES, "$1");
    }	
    closedir(D);
    @TMP{@DATES} = ();
    @UDATES = sort keys %TMP;
    if( $#UDATES < 0 ){
        print "Usage: $0 YYYYMMDD\n";
        exit 1;
    }
    foreach( @UDATES ){
      &outrow( $_ );
    }
}
