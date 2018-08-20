% Auswertung von Comsol-Daten
%
% mehrere Schnitte durch Temperatur- oder Geschwindigkeitsfeld werden gemittelt

% Datenfile
infile = '';
infile = input('Bitte geben Sie den Namen der einzulesenden Datei ein: ', 's');

% Daten laden
daten = load(infile);

% z-Vektor bestimmen (1. Spalte)
z = unique(daten(:,1));

% Anzahl der Schnitte
schnitte = size(daten,1)/size(z,1);

% Werte bestimmen (2. Spalte)
werte = reshape(daten(:,2),[size(z,1) schnitte]);


% Alle Schnitte plotten
figure(1); cla; hold on;
for i=1:schnitte
  plot(z,werte(:,i))
end
hold off;

% Mittelwert bilden und plotten
mittelwert = mean(werte,2);
figure(2); cla;
plot(z,mittelwert)

% Daten exportieren (gnuplot)
fid = fopen(['mittel_',infile], 'w');
fprintf(fid, '# x \t\t y\n');
for i=1:length(z)
  fprintf(fid, '%f \t %f\n', z(i), mittelwert(i));
end
fclose(fid);

return

n=input('Wieviele Messpunkte haben sie benutzt? ');

z=Daten(:,1);
z=z(1:n,1);

v=Daten(:,2);

clear ans
clear infile
clear Daten

a=input('Aus wievielen Profilen möchten Sie den Mittelwert berechnen? ')
v=reshape(v,200,a)

for i=1:n
    Profil(i)=mean(v(i,:));
end

clear ans
clear infile
clear Daten
clear i
clear a
clear n

% plot(z, 'DisplayName', 'z', 'YDataSource', 'z'); hold all; plot(Profil, 'DisplayName', 'Profil', 'YDataSource', 'Profil'); hold off; figure(gcf)
