infile=' ';
infile=input('Bitte geben Sie den Namen der einzulesenden Datei ein  ','s');

Daten=load(infile);

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

plot(z, 'DisplayName', 'z', 'YDataSource', 'z'); hold all; plot(Profil, 'DisplayName', 'Profil', 'YDataSource', 'Profil'); hold off; figure(gcf)
